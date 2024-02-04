class ShoppingCart:
    def add(self, request, product, **kwargs):
        quantity = kwargs.get('quantity', 1)
        texture_code = kwargs.get('texture_code', 1)
        price = kwargs.get('price', 0)
        length = kwargs.get('length', None)
        width = kwargs.get('width', None)
        needs_curtain_rod = kwargs.get('needs_curtain_rod', None)
        cornice_7 = kwargs.get('cornice_7', None)
        cornice_9 = kwargs.get('cornice_9', None)
        Gordeh = kwargs.get('Gordeh', None)
        Miane = kwargs.get('Miane', None)
        Tasho = kwargs.get('Tasho', None)
        Scouti = kwargs.get('Scouti', None)

        # متغیرهای دیگر...

        print(f"Added product: {product}, Quantity: {quantity}, Texture Code: {texture_code}, Price: {price}")
        print(f"Length: {length}, Width: {width}, Needs Curtain Rod: {needs_curtain_rod}")
        print(f"Cornice 7: {cornice_7}, Cornice 9: {cornice_9}, Gordeh: {Gordeh}, Miane: {Miane}")
        print(f"Tasho: {Tasho}, Scouti: {Scouti}")

# تست تابع add با تمام متغیرها
cart = ShoppingCart()
cart.add(request=None, product="TestProduct", quantity=3, texture_code=2, price=50, length=10, width=5, needs_curtain_rod=True,
         cornice_7="Cornice7", cornice_9="Cornice9", Gordeh="GordehValue", Miane="MianeValue", Tasho="TashoValue", Scouti="ScoutiValue")
