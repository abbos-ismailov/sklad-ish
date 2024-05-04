from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Mahsulot, XomashyoMahsulot, Store
# Create your views here.

class XomashyoGetApiView(APIView):
    permission_classes = [AllowAny, ]
    def post(self, request):
        data = request.data
        spending = [] ### bizga kerak mahsulotlar uchun list
        result = []
        for i in data:
            item = XomashyoMahsulot.objects.filter(mahsulot_id__kodi=i)
            for j in item:
                obj = {
                    "xomashyo": j.xomashyo_id.id,
                    "quantity_all": j.quantity * data[i],
                    "mahsulot_id": j.mahsulot_id
                }
                spending.append(obj)
            mahsulot = Mahsulot.objects.get(kodi=i)
            result.append(
                {
                    "product_name": mahsulot.name,
                    "product_qty": data[i], 
                    "product_materials": []
                }
            )
        xomashyolar = [] ### Xomashyolar uchun global list ochdik bazaga ozgartirish kirita olmaganimiz uchun
        for i in spending:
            xomashyolar.append(i["xomashyo"])
        xomashyolar = list(set(xomashyolar))

        materiallar = {} ### Storedagi hamma bizga kerak bolgan material (ip) uchun dict
        for i in xomashyolar:
            materiallar[i] = Store.objects.filter(xomashyo_id__id = i).order_by("created_time")


        for i in spending:
            mater = materiallar[i.get("xomashyo")] ### qaysi xomashyo kerak bolsa bazadan hammasini list sifatida olib keladik
            for j in range(len(mater)):
                if i["quantity_all"] < mater[j].remainder and mater[j].remainder and i["quantity_all"]:
                    new_obj = {
                        "warehouse_id": mater[j].id,
                        "material_name": mater[j].xomashyo_id.name,
                        "qty": i["quantity_all"],
                        "price": mater[j].price
                    }
                    mater[j].remainder -= i["quantity_all"] ### band qilingani uchun bazadan ayirib qoyamiz
                    i["quantity_all"] = 0 ### hamma keraklisini olganini bilib turish uchun nolga tengladik
                else: ### Agarda False qaytsa bazadagi borini berib yuboramiz
                    new_obj = {
                        "warehouse_id": mater[j].id,
                        "material_name": mater[j].xomashyo_id.name,
                        "qty": mater[j].remainder,
                        "price": mater[j].price
                    }
                    i["quantity_all"] -= mater[j].remainder
                    mater[j].remainder = 0 ### bazada qolmaganini bilib turish uchun nolga tengladik
                for n in result:
                    if n["product_name"] == i["mahsulot_id"].name and new_obj.get("qty"):
                        n.get("product_materials").append(new_obj)
                
                if i["quantity_all"] == 0:
                    break

            if i["quantity_all"]: ### agar nolga teng bolmasa Store dagi hamma mahsulot yetmagan boladi
                new_obj = {
                        "warehouse_id": None,
                        "material_name": mater[0].xomashyo_id.name,
                        "qty": i["quantity_all"],
                        "price": None
                    }
                for n in result:
                    if n["product_name"] == i["mahsulot_id"].name:
                        n.get("product_materials").append(new_obj)

        return Response(data={"result": result})
