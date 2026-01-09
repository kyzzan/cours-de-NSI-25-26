

1. HTML

HyperText Markup Language *langage de balise hypertexte*

un fichier `.html` est un fichier de texte( comme le markdown ).on ouvre un fichier de deux façons :

- le développeur => avec un éditeur de code (ex: VisualStudioCode)

- l'utilisateur => avec un navigateur 

le plus souvent les balises html sont en couple (ouvrante/fermante) mais il existe aussi des balises "opheline" :
- `<balises></balises>`
-`<Mabilise>`

la structure minimale d'une page web est :
```html
<!DOCTYPE html>
<html>


</html>
```

le site de référence pour les langages du web est le site des développeurs de Mozilla. 
[https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements)

Quelques balises à connaitre :
- `<body></body>`contient ce qui est visible sur la page
- `<head></head>`contient ce qui n'est pas visible sur la page
- `<h1></h1>` permet de faire des titres sur la page 
- `<p></p>`permet de faire un paragraphe
- `<a></a>`permet d'accrocher le curseur sur un lien 
- `<img>` pour insérer une image 
- `<ul></ul>` pour réaliser une liste sans ordre 
- `<ol></ol>` pour réaliser une liste ordonné 
- `<li></li>` pour insérer des items dans une liste 
- `<br>`pour casser la ligne 


les balises ouvrantes peuvent contenir des attributs défini sur le site de référence ou l'attribut `class=""`:<br>
`<mabalise attribut=""></mabalise>

pour donner le chemin relatif vers un fichier on utilise :
- `./` pour chercher dans le dossier courant 
- `../` pour chercher dans le dossier du desses 

2. CSS
cascading style sheet
[https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties)

pour définir du style il faut un sélecteur (élément html ou class), des accolades une propriété et une valeur 

```css
selecteur{
    propriete:valeur;
}

```

on peut écrire le css :
- dans le ficher html entre les balises`<style></style>`
- dans un fichier dédié avec l'extention `ccs` ; il faut ajouter une balise `<link ref>

il existe plus de 500 propriétés et encore d'avantage de valeurs possibles mais souvent , les valeurs sont :
- des couleurs (soit un nom soit un code comme rgb)