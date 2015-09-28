class Prueba06():
    def get_iguales(self, number_list, k):
        return [x for x in number_list if x==k]

    def get_multiplos(self, number_list, k):
        return [x for x in number_list if x%k==0]

    def get_mayores(self, number_list, k):
        return [x for x in number_list if x > k]

    def get_menores(self, number_list, k):
        return [x for x in number_list if x < k]
