# Exercice C : Fonctions et Boucles

## 📚 Objectifs
Apprendre les bases de la programmation en C à travers :
- L'utilisation de `printf`
- Les boucles `for` et `while`
- La création et l'appel de fonctions
- La manipulation de variables

---

## 🚀 Instructions étape par étape

### Étape 1 : Premier programme
Créer un fichier `main.c` avec une fonction `main` qui utilise `printf` pour écrire "Hello PLD !".

**Objectif :** Afficher un message simple à l'écran.

---

### Étape 2 : Analyse théorique
Créer un fichier `analyse.txt` et y répondre aux questions suivantes :

1. **Quelle bibliothèque doit-on inclure pour utiliser `printf` ?**
2. **Citer 2 autres fonctions de cette même bibliothèque** (pas besoin de les comprendre)
3. **Décomposer la signature de la fonction `main`** : Quels sont les 3 éléments qui composent la signature de la fonction `main` ?

---

### Étape 3 : Boucle for
Modifier votre `main.c` :

1. Déclarer un entier nommé `number` **au-dessus** du premier `printf`
2. Créer une boucle `for` qui imprimera "Tour {valeur de number}" jusqu'au tour 10
3. Utiliser `printf` avec le spécificateur `%d`

**Exemple de sortie attendue :**
```
Hello PLD !
Tour 1
Tour 2
...
Tour 10
```

---

### Étape 4 : Boucle while
À ce stade, la valeur de `number` doit être de 11.

Après la boucle `for`, ajouter une boucle `while` qui continue d'imprimer "Tour {valeur de number}" jusqu'au tour 20 inclus.

**Sortie attendue (suite) :**
```
Tour 11
Tour 12
...
Tour 20
```

---

### Étape 5 : Création d'une fonction ⚡ (+ difficile)
1. **Créer une fonction** avec la signature : `void multiply(int a, int b)`
2. Cette fonction doit imprimer le produit de la multiplication entre `a` et `b`
3. **Appeler cette fonction** dans `main` avec les paramètres 35 et 57
4. Afficher le résultat de 35 × 57

---

### Étape 6 : Enquête mystère 🕵️
**À quoi correspond le nombre imprimé à l'étape 5 ?**

*Indice : Demandez à d'autres étudiants sur le campus ! Ce nombre a une signification particulière...*

---

## 📁 Structure attendue du projet

```
i_already_love_C/
├── main.c          # Code source principal
├── analyse.txt     # Réponses aux questions théoriques
└── README.md       # Ce fichier
```

---

## 🛠️ Compilation et exécution

```bash
# Compiler le programme
gcc -Wall -pedantic -Werror -Wextra -std=gnu89 main.c -o program

# Exécuter le programme
./program
```

---

## 📖 Documentation et ressources

### Sites en français (sauf printf) pour vous aider :

1. **[IBM - Fonction main](https://www.ibm.com/docs/fr/i/7.5.0?topic=functions-main-function)**

2. **[Fonction printf en C](https://www.geeksforgeeks.org/c/printf-in-c/)**

3. **[Zeste de Savoir - Variables en C](https://zestedesavoir.com/tutoriels/755/le-langage-c-1/1042_les-bases-du-langage-c/4286_les-variables/)**

4. **[Zeste de Savoir - Boucles en C](https://zestedesavoir.com/tutoriels/755/le-langage-c-1/1042_les-bases-du-langage-c/4295_les-boucles/)**

5. **[Zeste de Savoir - Fonctions en C](https://zestedesavoir.com/tutoriels/755/le-langage-c-1/1042_les-bases-du-langage-c/4296_les-fonctions/)**





### Points clés à retenir :
- **Spécificateurs de format** : `%d` pour les entiers, `%s` pour les chaînes
- **Syntaxe des boucles** : `for(init; condition; increment)` et `while(condition)`
- **Déclaration de fonctions** : type de retour, nom, paramètres

---

## ✅ Critères de réussite

- [ ] Le programme compile sans erreur
- [ ] "Hello PLD !" s'affiche correctement
- [ ] Les boucles `for` et `while` fonctionnent comme attendu
- [ ] La fonction `multiply` est correctement implémentée et appelée
- [ ] Le fichier `analyse.txt` contient les bonnes réponses
- [ ] Vous avez découvert la signification du nombre mystère ! (passage au deuxième trimestre assuré)
