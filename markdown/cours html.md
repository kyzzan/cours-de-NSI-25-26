

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
- des tailles : plusieur unités sont possibles
    - `px` pour pixels
    - `em` relatif a la taille de la police 
    - `%` relatif a la taille de la page 

rem : quand le selecteur css et un element html ( par exemple `p`)
alors les propriétés s'appliquent à tous  les éléments de meme types 

pour différencier des elements de meme nature, on peut utiliser l'attribut `class` ou `id`. dans ce cas , le selecteur est le nom de la classe précédé d'un point ou le nom de l'identifiant précédé d'un `#`. 

rem le contenu d'un elemet html suit le principe du modèle en boite
[https://www.w3schools.com/css/css_boxmodel.asp](https://www.w3schools.com/css/css_boxmodel.asp)

trois propriété importante liée :
- `border`
- `padding`
- `marging`

rem : propriétés spécifique au texte :
- `text-align`
- `font`

il existe deux balises html universelles qui permetttent de regrouper des elements ou du texte 
- <div></div>
- <span></span>

3. Javascript

Ctrl + Shift + i pour obtenir la console

Il s'agit d'un langage de programmation comme Python mais initialement dédié au WEB.

C'est un langage prévu pour interagir avec une page HTML : le document
peut se représenter ainsi:

Imagesimplifiée du DOM (Document Object Model)
```
window
├── alert()
└── document
    ├── getElementById()
    ├── querySelector()
    │       ↓
    │   élément HTML
    │       ├── innerHTML
    │       ├── style
    │       │     ├── color
    │       │     ├── backgroundColor
    │       │     └── display
    │       └── addEventListener()
```




Le JS permet de rendre une page HTML plus dynamique notamment
grâce aux formulaires `<form></form>`.

Les éléments HTML interactifs sont généralement des `<input type="">`:
- button
- checkbox
- text
- range
- password ...


Pour écrire du JS on utilise les balises `<script></script>` et :
- on écrit directement le code dans le fichier HTML
- on écrit le code dans un fichier .js


Pour attraper un élément sur la page afin de la manipuler avec JS, on peut utiliser:
- `querySelector()`
- `getElementById()`


On écrira : 
```js
let elementHTML = document.querySelector(""); //avec un sélecteur css
let elementHTML = document.getElementById(""); // avec un id
```

La plupart des éléments HTML interactifs ont une propriété `value`.

```js
console.log(elementHTML.value);
```

JS est capable d'associer un évènement à un élément HTML:
- click
- change
- input
- mouseover ....


On utilise la méthode `addEventListener()`

```js
elementHTML.addEventListener("event", function(){
// faire qqchose
});
```