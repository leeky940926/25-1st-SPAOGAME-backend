import json

from django.db        import transaction
from django.views     import View
from django.http      import JsonResponse
from django.db.utils  import IntegrityError

from postings.models import (
    Comment,
    Posting
)

from products.models import (
    Category,
    Color,
    DetailedProduct,
    Image,
    Menu,
    Product,
    Size
)

from users.models    import User

class MenuView(View) :
    def post(self, request) :
        try :
            data = json.loads(request.body)

            Menu.objects.create(name=data['name'])

            return JsonResponse({'message' : 'Save Success'}, status=201)
        
        except KeyError : 
            return JsonResponse({'message' : 'KeyError'}, status=400)

    def get(self, request) :
        try :
            menu_lists = [{"id" : menu.id, "name" : menu.name} for menu in Menu.objects.all()]

            return JsonResponse({'menus' : menu_lists}, status=200)

        except AttributeError :
            return JsonResponse({'message' : 'AttributeError'}, status=400)
        
        except TypeError :
            return JsonResponse({'message' : 'TypeError'}, status=400)

class CategoryView(View) :
    def post(self, request) :
        try :
            data = json.loads(request.body)

            Category.objects.create(
                menu_id = data['menu_id'],
                name    = data['name']
            )

            return JsonResponse({'message' : 'Save Success'}, status=201)

        except KeyError : 
            return JsonResponse({'message' : 'KeyError'}, status=400)

        except IntegrityError :
            return JsonResponse({'message' : 'IntegrityError'}, status=200)

    def get(self, request, menu_name) :
        try :

            category_lists = [{'menu_id' : category.menu_id, 'category_id' : category.id} for category in Category.objects.\
                filter(menu_id=Menu.objects.get(name=menu_name))]

            return JsonResponse({'categories' : category_lists}, status=200)

        except AttributeError :
            return JsonResponse({'message' : 'AttributeError'}, status=400)
        
        except TypeError :
            return JsonResponse({'message' : 'TypeError'}, status=400)

class ProductView(View) :
    def post(self, request) :
        try :
            data        = json.loads(request.body)
            menu_id     = data['menu_id']
            category_id = data['category_id']
            name        = data['name']
            price       = data['price']
            description = data['description']
            quantity    = data['quantity']
            thumb_url   = data['thumb_url']
            img_urls    = data['img_urls']

            with transaction.atomic() :
                product = Product.objects.create(
                    menu_id             = menu_id,
                    category_id         = category_id,
                    name                = name,
                    price               = price,
                    description         = description,
                    quantity            = quantity,
                    thumbnail_image_url = thumb_url
                )

                urls = [Image(urls=url, product_id=product.id) for url in img_urls]

                Image.objects.bulk_create(urls)

            return JsonResponse({'message' : 'Save Success'}, status=200)

        except KeyError : 
            return JsonResponse({'message' : 'KeyError'}, status=400)

        except IntegrityError :
            return JsonResponse({'message' : 'IntegrityError'}, status=200)

    def get(self, request, menu_name, category_name) :
        try :
            offset   = int(request.GET.get('offset', 0)) 
            limit    = int(request.GET.get('limit', 15))
            order_id = int(request.GET.get('order_id', 0))

            order_dic = {
                0 : 'created_at',
                1 : '-price',
                2 : 'price',
                3 : 'name'
            }

            if limit > 20 :
                return JsonResponse({'message':'too much lists'}, status=400)
            
            goods = [{
                'id'           : product.id,
                'name'         : product.name,
                'price'        : product.price,
                'img_urls'     : product.thumbnail_image_url,
                'review_count' : product.posting_set.all().count(),
                'colors'       : [Color.objects.get(id=color['color_id']).name for color 
                in DetailedProduct.objects.filter(product_id=product.id).values('color_id')]
            } for product in Product.objects.filter(menu=Menu.objects.get(name=menu_name), 
                category=Category.objects.get(menu=Menu.objects.get(name=menu_name), name=category_name)).\
                order_by(order_dic[order_id])[offset:offset+limit]]

            return JsonResponse({'goods':goods}, status=200)

        except AttributeError :
            return JsonResponse({'message' : 'AttributeError'}, status=400)
        
        except TypeError :
            return JsonResponse({'message' : 'TypeError'}, status=400)

class DetailProductView(View) :
    def get(self, request, id) :
        try :      

            for product in DetailedProduct.objects.filter(product_id=id) :

                posting_info = [{
                    "posting_id"      : posting.id,
                    "posting_writer"  : User.objects.get(id=posting.user_id).name,
                    "posting_title"   : posting.title,
                    "posting_content" : posting.content,
                    "posting_image"   : [image.urls for image in Image.objects.filter(posting_id=posting.id)],
                    "posting_date"    : posting.created_at.strftime('%Y-%m-%d'),
                    "comment_info"    : [{
                        "posting_id"      : posting.id,
                        "comment_id"      : comment.id,
                        "comment_writer"  : User.objects.get(id=comment.user_id).name,
                        "comment_content" : comment.content,
                        "comment_date"    : comment.created_at.strftime('%Y-%m-%d')
                    } for comment in Comment.objects.filter(posting=posting.id).order_by('created_at')]
                } for posting in Posting.objects.filter(product_id=product.product_id).order_by('-created_at')]

            goods_detail = [{
                "product_id"    : id,
                "name"          : Product.objects.get(id=id).name,
                "price"         : Product.objects.get(id=id).price,
                "colors"        : [Color.objects.get(id=color['color_id']).name for color in DetailedProduct.objects.filter(product_id=id).values('color_id')],
                "size"          : [Size.objects.get(id=size['size_id']).name for size in DetailedProduct.objects.filter(product_id=id).values('size_id')],
                "image_list"    : [image.urls for image in Image.objects.filter(product_id=id)],
                "posting_info"  : posting_info,
                "posting_count" : Posting.objects.filter(product_id=id).count(),
            }]
                    
            return JsonResponse({'goods_detail' : goods_detail}, status=200)

        except AttributeError :
            return JsonResponse({'message' : 'AttributeError'}, status=400)
        
        except TypeError :
            return JsonResponse({'message' : 'TypeError'}, status=400)

class MainView(View) :
    def get(self, request) :
        try :
            product = [{
                "product_id" : product.id,
                "image"      : product.thumbnail_image_url
            } for product in Product.objects.all()]

            return JsonResponse({'message' : product}, status=200)

        except AttributeError :
            return JsonResponse({'message' : 'AttributeError'}, status=400)
        
        except TypeError :
            return JsonResponse({'message' : 'TypeError'}, status=400)
