ansd_mobile_app
===============

## Screenshots

![ansd_mobile_app screenshot](https://raw.github.com/aliounedia/ansd_mobile_app/master/screenshot/group_search.PNG "")
![ansd_mobile_app screenshot](https://raw.github.com/aliounedia/ansd_mobile_app/master/screenshot/search.PNG "")

Cette application a pour but de montrer comment utiliser l'api de ckan 
https://github.com/okfn/ckanclient pour recuperer des infortions sur le
datahub -http://datahub.io/.



Les developpeurs du https://github.com/okfn ont concu l'api qui 
permet de rechercher de facon tres simple dans le datahub toutes
les informations possibles .Le type de donnees retourne est 
generallement du jSON En quelque sotre une recherche sur le
datahub a partir d'un client 

ckan https://github.com/aliounedia/ansd_mobile_app/blob/master/api.py

pourrait donner comme resultat la structure suivante 


"resources": [
{
"cache_last_updated": null,
"cache_url": "",
"created": "2013-03-29T05:17:07.948745",
"description": "",
"format": "",
"hash": "",
"id": "a621d33f-d18e-475d-9606-b1f2fc1e423a",
"last_modified": "2013-03-29T05:17:11.777571",
"mimetype": "application/pdf",
"mimetype_inner": "",
"name": "",
"package_id": "b2e5ec1a-5818-4c89-8739-f6ece9d478cf",
"position": 0,
"resource_group_id": "50c0f488-4ea4-4958-88f5-5fa71c3df992",
"resource_type": "file",
"size": "197902",
"tracking_summary": {
"recent": 0,
"total": 0
},
"url": "http://www.ansd.sn/publications/conjoncturelles/ReperStat/
 ReperStat_01_12.pdf",
"webstore_last_updated": null,
"webstore_url": ""
}, 

Ces resultas peuvent etre reutilises afin d'extraitre  de vrais 
donneescomme des fichiers CSV par exemple que le developpeur 
pourrait utliser ditectement
ou le telecharger dans une base de donnees tier.
Voici un exemple simple qui extrait  le fichier CSV sur le 
datastore

https://github.com/aliounedia/ansd_mobile_app/blob/master/csv/download.py

Noter que cette cette structure simple a l'image du gestionnaire
de packet  - debian  - permet quasiment de tout faire avec les donnees
comme par exemple une utilisation dans une application 
jquery-mobile.

https://github.com/aliounedia/ansd_mobile_app
https://github.com/aliounedia/ansd_mobile_app/blob/master/api.py
https://github.com/aliounedia/ansd_mobile_app/blob/master/urls.py
https://github.com/aliounedia/ansd_mobile_app/blob/master/views.py

La plus grande difficulte comme Genova l'a dit tentot est davoir 
des donnees structurees. Pour cela il est indispensable de 
reflechir
avec des staticiens qui maitrisent les donnees car il y'a 
beaucoup d'informations et de codes qui ne parlent pas vraiment
a un informaticien
Nous avons besion de Vous!. Une fois que cette etape difficile 
sera 
teriminee nous pourrions en ce moment dire que du bon job a ete 
effetue.

Merci a Geno ,d'avoir bien volu nous associer a ce projet , 
j'ai hate de passer a la troisieme phase !
- Ad



