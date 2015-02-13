
# TODO list
- Site web / forum pour les cores participants -> voir réponse de Martha
- Contacter les potentiels cores particpants
- Répondre aux questions du sondage
- Récupérer les vidéos INA et AGORA
- Pré-traiter les corpus REPERE, INA et AGORA
  * REPERE : 
    + Extraction des features images
  * INA et AGORA :
    + Découpage des ensembles de dev et de test
    + Extraction des noms écrits
    + Transcription de la parole + détection des entités nommées
    + Ré-encodage video si besoin
    + Segmentation en plan
    + Diarization des locuteurs
    + Distance entre track de visages (détection, tracking, flandmark, alignement, HoG, projection)
- Préparer un script de fusion pour la baseline
  * En entrée: diarization audio, clustering des tracks de visages, nom écrits
  * En sortie: Segments temporels avec un nom associé + preuves
  * Process :
    + Propagation des noms écrits sur la diarization audio (Fusion tardive type interspeech 2012)
    + Association un à un des cluster de visage avec les locuteurs de la diarization
    + Sélection des tours de parole et des visages (nommés par le même nom) co-occurants
    + Extraction d'une preuve pour chaque personne/vidéo
- Interface/script de soumission (avec possibilité de modification des soumissions)
- Script d'extraction des annotations fournies vers des annotations en plan
- Script de recherche de plan
  * En Entrée : requête (nom, date, score de confiance) et de la liste des plans annotés par les particpant
  * En Sortie : Liste ordonnée de plan
  * Process : 
- Script d'évaluation
  * En Entrée : Liste ordonnée de plan / (nom, date)
  * En Sortie : score 
  * Process : 
- Post-annotation 
	* Constitution des jeux d'annotation : Pour chacun des participants à tour de rôle, on prend un nom et un vidéo au hasard (non annoté) dans leurs soumissions et l'on choisis les XX plans à annoté pour tous les participants. Un jeu d'annotation correspond aux XX plans sont choisis en fonction du score de confiance des particpants et de la distance entre le nom de la requête et le nom proposé par le participant
	* Un jeu d'annotation est fournis à un annotateur qui annote l'ensemble des plans du jeu
	* Annotation en 3 phases:
		+ Vérification des preuves : on montre le segment vidéo est l'on valide ou pas le nom associé
		+ Association entre un visage hypothèse est une preuve : une preuve et un ensemble d'imagette correspondant aux plans hypothèses sont montrés, l'utilisateur doit cliqué sur les visages des vignettes correspondant à la preuve
		+ Vérification que le visage parle : chaque visage 
- Adjudication








