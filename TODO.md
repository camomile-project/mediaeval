
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
- Script d'extraction des annotations fournis
- Outils de post-annotation / adjudication







