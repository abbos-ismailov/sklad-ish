from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Product, MaterialProduct, Store


class MaterialGetApiView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def post(self, request):
        data = request.data
        # TODO: bizga kerak mahsulotlar uchun list
        spending = []
        result = []
        for i in data:
            item = MaterialProduct.objects.filter(product_id__code=i)
            for j in item:
                obj = {
                    "material": j.material_id.id,
                    "quantity_all": j.quantity * data[i],
                    "product_id": j.product_id,
                }
                spending.append(obj)
            product = Product.objects.get(code=i)
            result.append(
                {
                    "product_name": product.name,
                    "product_qty": data[i],
                    "product_materials": [],
                }
            )
        # TODO: Xomashyolar uchun global list ochdik bazaga ozgartirish kirita olmaganimiz uchun
        materials = []
        for i in spending:
            materials.append(i["material"])
        materials = list(set(materials))
        # TODO: Storedagi hamma bizga kerak bolgan material(ip) uchun dict
        material_dict = {}
        for i in materials:
            material_dict[i] = Store.objects.filter(material_id__id=i).order_by(
                "created_time"
            )
        for i in spending:
            mater = material_dict[i.get("material")]
            for j in range(len(mater)):
                if (
                    i["quantity_all"] < mater[j].remainder
                    and mater[j].remainder
                    and i["quantity_all"]
                ):
                    new_obj = {
                        "warehouse_id": mater[j].id,
                        "material_name": mater[j].material_id.name,
                        "qty": i["quantity_all"],
                        "price": mater[j].price,
                    }
                    mater[j].remainder -= i["quantity_all"]
                    # TODO: hamma keraklisini olganini bilib turish uchun nolga tengladik
                    i["quantity_all"] = 0
                else:
                    new_obj = {
                        "warehouse_id": mater[j].id,
                        "material_name": mater[j].xomashyo_id.name,
                        "qty": mater[j].remainder,
                        "price": mater[j].price,
                    }
                    i["quantity_all"] -= mater[j].remainder
                    # TODO: bazada qolmaganini bilib turish uchun nolga tengladik
                    mater[j].remainder = 0
                for n in result:
                    if n["product_name"] == i["product_id"].name and new_obj.get("qty"):
                        n.get("product_materials").append(new_obj)
                if i["quantity_all"] == 0:
                    break
            # TODO: agar nolga teng bolmasa Store dagi hamma mahsulot yetmagan boladi
            if i["quantity_all"]:
                new_obj = {
                    "warehouse_id": None,
                    "material_name": mater[0].xomashyo_id.name,
                    "qty": i["quantity_all"],
                    "price": None,
                }
                for n in result:
                    if n["product_name"] == i["product_id"].name:
                        n.get("product_materials").append(new_obj)
        return Response(data={"result": result})
