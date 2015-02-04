
# TODO list

- [ ] Interface/script de soumission (avec possibilité de modification des soumissions)
- [ ] Script d'extraction des annotations fournis
- [ ] Outils de post-annotation / adjudication -> jeu ?

#### Jeux pour la post annotation
- Trouver tous les images d'une personne dans un pêle-mêle :
  * On montre un exemple d'image + le nom associé (prealablement vérifié)
  * On affiche un pêle-mêle d'image 
  * L'utilisateur doit sélectionner le plus vite (???) possible les images de la personnes cible
  * Pour les images non sélectionnées mais faisant partie de l'hypothèse d'un participant -> adjudication
- Blind test visuel: retrouver le nom d'une personne apparaissant dans une image le plus vite possible sans ce tromper
- Puzzle: 
  * On affiche un pêle-mêle d'images avec les preuves (dejà vérifiées) + des hypothèses
  * On demande à l'utilisateur de regrouper les images de la même personnes dans un sac
  * On nomme les sacs par le nom de la/les preuves qu'il y a dedans -> si 2 preuves de personnes differentes dans un sac : adjudication
- Récompense lors du workshop Mediaeval pour les meilleurs annotateurs

## Corpus REPERE
- [ ] Extraction des features images

## Autre corpus (INA, UPC):
- [ ] Découpage des ensembles de dev et de test
- [ ] Extraction des noms écrits
- [ ] Transcription de la parole + détection des entités nommées
- [ ] Ré-encodage video si besoin
- [ ] Segmentation en plan
- [ ] Diarization des locuteurs
- [ ] Diarization des visages (détection, tracking, flandmark, alignement, HoG)

## Système de fusion de base fournit :
- Propagation des noms écrits sur la diarization audio (Fusion tardive type interspeech 2012)
- Propagation des noms des locuteurs vers les visages
- Sélection des tours de parole et des visages (nommés par le même nom) co-occurants

