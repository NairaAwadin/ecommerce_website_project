from django.conf import settings
from .models import product

class panier:
    def __init__(self, request):
        self.session = request.session
        panier = self.session.get(settings.CART_SESSION_ID)
        if not panier:
            panier = self.session[settings.CART_SESSION_ID] = {}
        self.panier = panier
       # self.panier(product_id) == {
       # 'name': product.nom,
       # 'price': float(product.prix),
        #'quantite': 1


    def ajouter(self, product_id, quantite=1):
        product_id = str(product_id)
        if product_id in self.panier:
            self.panier[product_id]['quantite'] += quantite
        else:
            self.panier[product_id] = {'quantite': quantite, 'price': str(product.objects.get(id=product_id).price)}
        self._sauvegarder()

    def supprimer(self, product_id):
        product_id = str(product_id)
        if product_id in self.panier:
            del self.panier[product_id]
            self._sauvegarder()

    def _sauvegarder(self):
        self.session[settings.CART_SESSION_ID] = self.panier
        self.session.modified = True

    def __iter__(self):
        products_ids = self.panier.keys()
        products = product.objects.filter(id__in=products_ids)
        panier = self.panier.copy()
        for product in products:
            panier[str(product.id)]['product'] = product
        for item in panier.values():
            item['price'] = (item['price'])
            item['total'] = item['price'] * item['quantite']
            yield item

    def vider(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

        # trouver comment afficher le prix total

    