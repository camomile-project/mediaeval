# TODO list

## Inscription (avant le 28/02)
- Site web / forum pour les cores participants -> voir réponse de Martha
- Contacter les potentiels cores participants de REPERE et Camomile avec un mail perso
- Répondre aux questions du sondage
- Faire le proposal en version longue

## Données (avant le 1/04)
- Récupérer les vidéos INA et AGORA
- Pré-traiter les corpus REPERE, INA et AGORA
    * REPERE : 
       + Extraction des features images
    * INA et AGORA : 
       + Extraction des noms écrits
       + Transcription de la parole + détection des entités nommées
       + Ré-encodage video si besoin
       + Segmentation en plan
       + Diarization des locuteurs
       + Distance entre track de visages (détection, tracking, flandmark, alignement, HoG, projection)
  
## Système de fusion baseline (avant le  1/04)
 - En entrée : diarization audio, clustering des tracks de visages, nom écrits
 - En sortie : Segments temporels avec un nom associé + preuves
 - Process :
    * Propagation des noms écrits sur la diarization audio (Fusion tardive type interspeech 2012)
    * Association un à un des cluster de visage avec les locuteurs de la diarization
    * Sélection des tours de parole et des visages (nommés par le même nom) co-occurants
    * Extraction d'une preuve pour chaque personne/vidéo

## Système de fusion Limsi (avant le 1/07)
- Extraction descripteur de visage qui parle
- Extraction des matrices hvh, svs, svh normalisées
- Vérifier le script de clustering aglomératif contraint
- tester un clustering K-Means contraint

## Système d'annotations (avant le 01/07)
- Script de constitution des jeux d'annotations :
	* Pour chacun des participants à tour de rôle, on prend un nom et une vidéo au hasard (non annoté) dans leurs soumissions
	* On choisis l'ensemble des XX premiers plans proposé par les participants -> un jeu d'annotations 
- Script de remplissage des queues pour l'annotation
- Interface d'annotation en 3 phases :
	* Vérification des preuves : L'annotateur doit cliquer sur le visage correspondant au nom affiché
	* Association entre un visage hypothèse est une preuve : 
		+ une preuve et un ensemble d'imagette correspondant aux plans hypothèses sont montrés. 
		+ l'utilisateur doit cliquer sur les visages des vignettes correspondant à la preuve
	* Vérification que les visages sélectionnés dans l'état précédente parle bien dans le plan.
		+ réduire la liste des vérifications à faire avec le score de la matrice svh

## Evaluation
- Choisir le format des données entrées / sorties (**avant le 28/02**)
- Interface/script de soumission (avec possibilité de modification des soumissions) (**avant le 01/05**)
- Script d'extraction des annotations fournies (REPERE, ...) vers des annotations en plan (**avant le 01/04**)
- Script de recherche de plan  (**avant le 1/07**)
   * En Entrée : requête (nom, date, score de confiance) et de la liste des plans annotés par les particpant
   * En Sortie : Liste ordonnée de plan
   * Process : 
- Script d'évaluation  (**avant le 1/04**)
   * En Entrée : Liste ordonnée de plan / (nom, date)
   * En Sortie : score 
   * Process : 
- Adjudication: (**avant le 1/08**)
   * Produire la liste des erreurs commit par les participants
   * Affichage d'une vidéo + timeline avec la diff entre la référence et une soumission
	







