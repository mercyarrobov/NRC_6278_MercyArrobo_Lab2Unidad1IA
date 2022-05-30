#Importación de Queue
from queue import Queue

class Grafo:  
    
    """
    Una clase para representar a un grafo

    ...

    Atributos
    ----------
    m_num_de_nodos : int
        número de nodos
    m_nodos : int
        rango de nodos
    m_directo : boolean
        directo o no directo 
    m_list_ady : mutable
        Defino el diccionario para implementar la lista adyacencia

    Metodos
    -------
    agregar_aristas(self, nodo1, nodo2, peso=1):
        Añadir aristas al grafo
    imprimir_lista_de_adj(self):
        Imprime la representación del grafo
    bfs_traversal(self, nodo_inicial):
        Imprime el recorrido del grafo apartir de un nodo dado
    """
     #Constructor
    def __init__(self, num_de_nodos, directo=True):
        
        '''
        Constructor inicializador de la clase grafo.

            Parameters:
                m_num_de_nodos : int
                    número de nodos
                m_nodos : int
                    rango de nodos
                m_directo : boolean
                    directo o no directo 
                m_list_ady : mutable
                    Defino el diccionario para implementar la lista adyacencia
        '''
        
        #Número de aristas
        self.m_num_de_nodos = num_de_nodos 
        #Inicializa el rango de los nodos
        self.m_nodos = range(self.m_num_de_nodos)
        #Definir el tipo de un grafo
        self.m_directo = directo
        # Lista de adyacencia usando diccionario
        self.m_list_ady = {nodo: set() for nodo in self.m_nodos}  
        
    def agregar_aristas(self, nodo1, nodo2, peso=1):
        
        """
        Función que agrega una arista al grafo

        Parámetros
        ----------
        nodo1 : int
            nodo de partida
        nodo2 : int
            nodo de llegada
        peso : int
            peso del nodo
            
        """
        
        #Añade la arista del nodo1 al nodo2"""
        self.m_list_ady[nodo1].add((nodo2, peso))

        #Si un grafo es no dirigido, añade la misma arista
        if not self.m_directo:
            #Pero también en la dirección opuesta
            self.m_list_ady[nodo2].add((nodo1, peso))