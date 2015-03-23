# TODO list

## Inscription (avant le 28/02)
- Site web / forum pour les participants -> voir réponse de Martha
- Répondre aux questions du sondage
- Nom d'un interlocuteur pour ELDA dans le short proposal
- Compléter le fichier task_description

## Données (avant le 1/05)

**Problème avec les données AGORA : les waves sont déjà téléchargeable avec les trs et l'identité des locuteurs** : 
 - Voir si tous les corpus a été transcrit, si non on réduit le test à la partie non transcrit -> il nous faut une transcription auto  + détection des noms de personnes auto

**Problème avec les données AGORA : il n'y a pas d'accord pour l'utilisation des images, seulement pour l'audio**

- Récupérer les vidéos INA et AGORA
	* INA : attendre le serveur Quaero
	* AGORA : 
		+ Johann : j'ai créer un compte sur metashare mais il est noté comme désactivé, j'ai envoyé un mail à Javier pour lui demander quoi faire
		+ Réponse de Ramon : We still did not upload the Agora data. We are planning to do so as soon as possible. I will inform you later this week.
- Vérifier le protocole pour les futurs participants (lien, documents à remplir)
- Pré-traiter les corpus REPERE, INA et AGORA
	* INA et AGORA : 
		+ Ré-encodage des vidéos si besoin ???
		+ Extraction des noms écrits
		+ Transcription de la parole + détection des entités nommées   ???? obligatoire ????
		+ Segmentation en plan
		+ Matrice de distances entre track de visages 
	* REPERE, INA et AGORA : 
		+ Diarization audio (REPERE ???)
		+ Matrice de distance entre tours de parole ???
		+ Matrice de distance entre visage et tours de parole ???

## Système de fusion baseline (avant le  1/05)
- En entrée : diarization audio, clustering des tracks de visages, nom écrits
- En sortie : Segments temporels avec un nom associé + preuves
- Process :
    * Propagation des noms écrits sur la diarization audio (Fusion tardive type interspeech 2012)
    * Association un à un des cluster de visage avec les locuteurs de la diarization
    * Sélection des tours de parole et des visages (nommés par le même nom) co-occurants
    * Extraction d'une preuve pour chaque personne/vidéo

## Système de fusion Limsi (avant le 1/07)
- Extraction descripteurs visages qui parlent
- Calcul des matrices hvh, svs, svh normalisées
- Vérifier le script de clustering agglomératif contraint
- Tester un clustering K-Means contraint

## Système d'annotations (avant le 01/07)
- Script de constitution des jeux d'annotations :
	* Pour chacun des participants à tour de rôle, on prend un nom+vidéo au hasard (non annoté) dans leurs soumissions
	* On choisis l'ensemble des XX premiers plans proposé par les participants -> un jeu d'annotations 
- Annotation en 3 phases :
	* Vérification des preuves
	* Identification des visages sur des vignettes à partir d'un visage témoin (une preuve)
	* Vérification que les visages sélectionnés dans l'état précédente parle bien dans le plan courant.
- Choisir la procédure du choix de l'ordre du type d'annotation (preuves, visages, visages parlant) à effectuer 
- Script de remplissage des queues pour l'annotation
- Backup de la base

## Annotation par le LIG du corpus INA
- Développement d'une interface d'annotation des visages (**avant le 1/06**)
- Active learning annotation pendant le mois de **juin** par le LIG:
	1. Le back-end du LIG sélectionne des shots à annoter
	2. On présente une liste de shot à un annotateur.
	3. Il vérifie si la personne visée par l'annotation est bien présente dans les shots
	4. Retour au 1. avec les nouvelles annotations en entrées en plus

## Evaluation
- Choisir le format des données entrées / sorties (**avant le 28/02**)
- Script d'extraction des annotations fournies (REPERE, ...) vers des annotations en plan (**avant le 01/05**)
- Script de classement des plans indéxés  (**avant le 1/05**)
    * En Entrée : requête (nom, date), et la liste des plans annotés par un participant
    * En Sortie : Liste ordonnée de plan
    * Process : 
    	1. Recherche des noms proposés proche du noms de la requête
    	2. Classement des plans des noms proches en fonction du score de confiance associé
- Script d'évaluation  (**avant le 1/05**)
	* En Entrée : pour chaque requête (nom, date) : une liste de plan ordonnée et les plans annotés correspondants
	* En Sortie : score MMAP@n
	* Process : 
		1. On calcul de la precision moyenne à n pour une requête (nom, date), avec P(k) qui est égale à la précision des kième premiers éléments de la liste :
$$ ap@n = \sum_{k=1}^n P(k) / min(m, n)  $$
		2. On calcul la MAP@n pour une personne sur V vidéos où elle apparait :
$$ MAP@n = \sum_{v=1}^V ap@n_v / V $$
		3. On calcul la MMAP@n total sur l'ensemble des personnes:
$$ MMAP@n = \sum_{i=1}^N MAP@n_i / N $$
- Interface/script de soumission (avec possibilité de modification des soumissions) (**avant le 01/06**)
- Interface d'adjudication: (**avant le 1/08**)
	* Dans l'interface, afficher une vidéo + timeline avec la diff entre la référence et la soumission
	







