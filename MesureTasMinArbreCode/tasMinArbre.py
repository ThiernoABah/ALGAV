import cle

#Arbre binaire
class TasMinArbre:
    def __init__(self, data):

        self.left = None
        self.right = None
        if data is None :
            self.data = None
        else :
            self.data = data
        
#renvoie le nombre de noeud qu'à le sous arbre enraciné en ce noeud
    def NbNoeud(self):
        if self.right is None and self.left is None :
            return 1
        elif self.right == None :
            return 1 + self.left.NbNoeud()
        elif self.left == None :
            return 1 + self.right.NbNoeud()
        else :
            return 1 + self.right.NbNoeud() + self.left.NbNoeud()
#Ajoute l'élement data dans un arbre
    #j'ai fais des retourne parce que ça ne s'arrête pas sinon tu me diras quoi mettre sinon.
    def Ajout(self, data):
        if self.data is not None:
            if self.data.inf(data) :
                if self.left is None :
                    self.left = TasMinArbre(data)
                    return True
                if self.right is None:
                    self.right = TasMinArbre(data)
                    return True
                if self.left.NbNoeud() >= self.right.NbNoeud():
                    self.right.Ajout(data)
                    return True
                if self.left.NbNoeud() < self.right.NbNoeud():
                    self.left.Ajout(data)
                    return True
            else :
                valeur = self.data
                self.data = data
                self.Ajout(valeur)
                return True

        else:
            self.data = TasMinArbre(data)
            return True


    # lorsqu'on ajoute un node
    def ajoutNode(self,data):
        if self.data is not None :
            if self.data.inf(data.data):
                if self.left is None:
                    self.left = data
                    return True
                if self.right is None:
                    self.right = data
                    return True
                if self.left.NbNoeud() >= self.right.NbNoeud():
                    self.right.ajoutNode(data)
                    return True
                if self.left.NbNoeud() < self.right.NbNoeud():
                    self.left.ajoutNode(data)
                    return True
            else:
                valeur = self
                self = data
                self.ajoutNode(valeur)
                return True
        else :
            self = data
            return True


    def prefixePrint(self):
        if self.left:
            self.left.prefixePrint()
        if self.right:
            self.right.prefixePrint()
        print(self.data)

#Supprime l'élement le plus petit de l'arbre
    def supprMin(self):
        if self.data is None:
            return False
        else:
            add = union(self.left, self.right)
            return add


    def ajoutArbre(self, arbre):
        if arbre.right is not None :
            self.ajoutArbre(arbre.right)
        if arbre.left is not None :
            self.ajoutArbre(arbre.left)
    
        self.Ajout(arbre.data)
            

#Fais l'union de deux arbres
def union(arbre1, arbre2) :
    if arbre1 is None :
        return arbre2
    if arbre2 is None :
        return arbre1
    else :
        if arbre1.data.inf(arbre2.data) :
            arbre1.ajoutArbre(arbre2)
            return arbre1
        else :
            arbre2.ajoutArbre(arbre1)
            return arbre2



#Construction itérative d'un arbre à partir d'une liste d'élement
def consIter(liste) :
    if(len(liste)>0):
        racine = TasMinArbre(liste[0])
        for i in range(1,len(liste)):
            racine.Ajout(liste[i])
        return racine
    return None

def main():
    a=cle.Cle("0x9c1f03a0d9cf510f2765bd0f226ff5dc")
    b=cle.Cle("0x10fd1015413104a2f26018d0ab77a727")
    c=cle.Cle("0x2e73d8ce4bd45923286e966bc8cf2d95")
    d=cle.Cle("0x767accd0c60c603f71a68be994019c7e")
    e=cle.Cle("0x34c63c08abab99722b945e57081288e7")
    f=cle.Cle("0x6d481adc2aeed025f0374a5982b5c23c")
    root = TasMinArbre(a)
    root.Ajout(b)
    root.Ajout(c)
    root.Ajout(d)
    root.Ajout(e)
    root.Ajout(f)
    
    a=cle.Cle("0x9a5cdb45f1951a3a82b09af737fdc9aa")
    b=cle.Cle("0x53f7ffe901f3686b875af337039ee262")
    c=cle.Cle("0xa89aa39aa55e5bb5fb33a1802b248207")
    d=cle.Cle("0x8aefe5f306ac962bcbdb63aeb58d1e35")
    e=cle.Cle("0x85c3d80bfe89b91033b23cd659cddb08")
    f=cle.Cle("0x45484c820aee4c04ef89c1db9bb3eaf5")
    root2 = TasMinArbre(a)
    root2.Ajout(b)
    root2.Ajout(c)
    root2.Ajout(d)
    root2.Ajout(e)
    root2.Ajout(f)
    
    
    arbre = union(root,root2)
    
    print(arbre.NbNoeud())


if __name__ == "__main__":
    main()