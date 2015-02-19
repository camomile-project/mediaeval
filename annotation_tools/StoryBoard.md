# StoryBoard

## Annotation des preuves OCR

#### Informations en entrée : 
 - nom de la personne
 - nom de la vidéo + timestamp où le nom est écrit à l'écran
 - nom de la vidéo + timestamp où apparait la personne
 
#### Scénario :
 - On affiche le nom de la personne correspondant à la preuve.
 - On affiche la vidéo où le nom est écrit à l'écran, calé sur le timestamp fourni.
 - On affiche la vidéo où apparait la personne, calé sur le timestamp fourni.
 - On demande à l'utilisateur de cliquer sur le visage correspondant au nom.
 - Si l'annotateur ne voit pas la personne correspondante dans l'image affiché, elle peut lire le plan de la vidéo pour trouver une meilleur image.
 - Si elle ne trouve pas la personne, elle clique sur un bouton.

## Annotation des preuves ASR

#### Informations en entrée : 
 - nom de la personne
 - nom de la vidéo + timestamp où le nom est prononcé
 - nom de la vidéo + timestamp où apparait la personne
 - La phrase prononcée et le nom taggé

#### Scénario :
 - On affiche le nom de la personne correspondant à la preuve.
 - On affiche le segment vidéo où le nom est prononcé, calé sur le timestamp fourni -10 secondes.
 - On affiche la vidéo où apparait la personne, calé sur le timestamp fourni.
 - On joue la vidéo pendant 20 secondes
  - On demande à l'utilisateur de cliquer sur le visage correspondant au nom.
 - Si l'annotateur ne voit pas la personne correspondante dans l'image affiché, elle peut lire le plan de la vidéo pour trouver une meilleur image.
 - Si elle ne trouve pas la personne, elle clique sur un bouton.
 
## Vérification de l'identité des visages

- On affiche l'image d'une preuve + un nom.
- On affiche une liste d'imagette correspondant au centre de chacun des plans à annoter pour une vidéo.
- Si la personne correspondante est visible, l'annotateur clique sur son visage.
- Si la personne n'est pas visible, l'annotatuer peut cherche une meilleur image dans le plan en lisant la vidéo.
- Si la personne n'apparait pas dans le plan, elle clique sur un bouton.


## Vérification que les visages parlent

- On affiche un plan avec un visage entouré (celui sur lequel l'annotateur à cliqué dans l'étape précédente).
- L'annotateur joue la vidéo est vérifie si la personne parle dans le plan.
