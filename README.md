# API NEWS V4
This is the official doc of the news engine provided by Qwant Research.


# Features:

So far, the following features are developped

## Search Engine of News:

Given a query, return the top N results that fit the most.
Route: 
>localhost:8000/v1/search
Accepted request : GET

The different accepted parameters are the following :
**Required params:**
> *"query"* : The query to search news for *

**Optional params**

  > - *source*: The source of the news to look from
   > - *language*: The language in which the news is
   > - *count*: How many news should be returned
   > - *offset*: The offset of the searcher
   > - *fromDate* : Minimum date to look for
   >  - *toDate* : Minimum date to look for

Example query : 
> http://0.0.0.0:8000/v1/search/?query=test&count=1
retun : 
	  

      {
        status: "OK",
        message: "",
        result: {
	        root: {
		        id: "toplevel",
		        relevance: 1,
		        fields: {
		        totalCount: 552
		        },
	        coverage: {
		        coverage: 100,
		        documents: 17542,
		        full: true,
		        nodes: 1,
		        results: 1,
		        resultsFull: 1
		        },
	        children: [
	        {
		        id: "id:newsv2:newsv2::50a8d6fe0d6a8ea7",
		        relevance: 0.22618627403079472,
		        source: "newsv2",
		        fields: {
			        sddocname: "newsv2",
			        body: "édition abonné Profitant des technologies de séquençage de l’ADN, des start-up américaines proposent aux particuliers, à grand renfort de marketing, une gamme de tests évaluant le risque pour eux d’avoir un enfant malade. Le Monde | 23.05.2018 à 05h42 | Par Chloé Hecketsweiler (San Francisco, Californie, envoyée spéciale) A San Francisco (Californie), dans un ancien bâtiment industriel reconverti en temple de la génétique high-tech, les échantillons arrivent dans de simples enveloppes FedEx. Des techniciens en blouse blanche et gants bleus les déballent à la chaîne, leur travail est ponctué par le « bip » des lecteurs de code-barres. Une fois identifiés, les tubes sont alignés en rangs dans de petits casiers multicolores et ils sont mis au frais dans de grandes armoires réfrigérées. Dans quelques jours, l’ADN extrait de ces quelques millilitres de sang ou de salive aura livré ses secrets. En 2017, environ 150 000 échantillons ont ainsi été expédiés chez Invitae, l’une des nombreuses start-up à surfer sur la vague des tests génétiques. Ce chiffre devrait presque doubler cette année, en raison de l’engouement des futurs parents conquis par la promesse d’un bébé parfait. Estimées à 2 milliards de dollars (1,7 milliard d’euros) aux Etats-Unis, les ventes de tests génétiques prénataux devraient bondir de 10 % par an d’ici à 2021. Aux côtés d’Invitae, une dizaine de start-up (Natera, Counsyl et Verinata…) sont parties à la conquête de ce marché. A grand renfort de marketing, ces laboratoires commercialisent des tests destinés à évaluer le risque pour un couple en bonne santé de donner naissance à un enfant mala­de, ou à sélectionner les embryons lors d’une fécondation in vitro (FIV). Avec les progrès spectaculaires des technologies de séquença­ge, l’univers futuriste de Bienvenue à Gattaca – un film de 1997 qui met en scène des humains au génome irréprochable – ne semble plus si loin. Lire les 3 milliards de « lettres » (A, T, C, G) qui composent un génome humain coûte moins de 1 000 dollars (850 euros), contre 1 million de dollars il y a dix ans. Et quelques centaines de dollars suffisent aujourd’hui pour une analyse ciblée de gènes. « L’Amazon des tests génétiques » Invitae, qui ambitionne de devenir « l’Amazon des tests génétiques »,...",
			        category: "science",
			        category_id: "0",
			        country: "science",
			        description: "Profitant des technologies de séquençage de l’ADN, des start-up américaines proposent aux particuliers, à grand renfort de marketing, une gamme de tests évaluant le risque pour eux d’avoir un enfant malade.",
			        hostsite: "www.lemonde.fr",
			        index_date: "2018-05-23 04:35:50",
			        entities: [
			        "C",
			        "Counsyl",
			        "Invitae",
			        "A",
			        "Verinata",
			        "Chloé Hecketsweiler",
			        "–",
			        "G",
			        "Californie",
			        "San Francisco",
			        "T",
			        "Natera",
			        "Amazon",
			        "Etats-Unis"
			        ],
			        lastmod: "2018-05-23 04:35:50",
			        media: "https://img.lemde.fr/2018/05/22/274/0/1200/599/644/322/60/0/d3ebf57_21695-awa38f.dgna.jpg",
			        published_date: "2018-05-23 05:42:30",
			        qrank: 78,
			        timestamp: 1527050150,
			        title: "Tests génétiques : bientôt des bébés à la carte ?",
			        url: "https://www.lemonde.fr/entreprises/article/2018/05/23/tests-genetiques-bientot-des-bebes-a-la-carte_5302991_1656994.html",
			        language: "fr",
			        authors: [ ],
			        documentid: "id:newsv2:newsv2::50a8d6fe0d6a8ea7"
		        }
        }
        ]
        }
        }
        }

## Get Top entities:
The goal of this route is to provide today's trending entities. The goal is not to give the same entities everyday, but really capture the personality trending today and not yesterday.
**Route**:
> http://0.0.0.0:8000/v1/entities/

http://0.0.0.0:8000/v1/entities/?country=fr&number=5
All your files are listed in the file explorer. You can switch from one to another by clicking a file in the list.
**Required params:**
> "country" : Define the country of search.
**Optional params**

  > - *category*: get the trending personality of a category ( Not tested)
   > - *count*: How many entities should be returned
  
####  Example:

Query: 
> http://0.0.0.0:8000/v1/entities/?country=fr&count=5

		{
		   status:  "1",    
		   message:  "",
		   result:[
		       "Agnès Buzyn",
		       "Anne Hidalgo",
		       "Antoine Griezmann",
		       "Badra",
		       "Benoît Hamon"
		    ]
		}



## Get News cluster:
The goal of this route is to provide group of news that speaks about a similar topic

**Route**:
> http://0.0.0.0:8000/v1/clusters/

**Required params:**
> "country" : Define the country of search.
**Optional params**

   > - *count*: How many entities should be returned
   > - *lang* : Language of the news in the cluster
  
####  Example:

Query: 
> http://0.0.0.0:8000/v1/clusters/?count=5

		{
		   status:  "1",    
		   message:  "",
		   result:[
		       "Agnès Buzyn",
		       "Anne Hidalgo",
		       "Antoine Griezmann",
		       "Badra",
		       "Benoît Hamon"
		    ]
		}
