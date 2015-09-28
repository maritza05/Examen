class Prueba06():
    def valores_listas(self, number_list, k):
        num_iguales = [x for x in number_list if x==k]
        return num_iguales

    def get_multiplos(self, number_list, k):
        num_multiplos = [x for x in number_list if x%k==0]
        return num_multiplos

    def get_mayores(self, number_list, k):
        num_mayores = [x for x in number_list if x > k]
        return num_mayores

    def get_menores(self, number_list, k):
        num_menores = [x for x in number_list if x < k]
        return menores
