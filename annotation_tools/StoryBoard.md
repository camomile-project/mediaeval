# StoryBoard

The goal is to correct submissions of participants. The process is devided into multiple annotation tasks

## Evidences annotation

#### Input datas: 
 - Person name
 - A shot of a video
 - Evidence type (audio for pronounced names, video for written names)
 
#### Scenario :
 - Show the name of the person used as evidence
 - Show the shot of the video to annotate (+/- 5 seconds for audio evidence)
 - Ask to the annotator:
   * to play the video to find the evidence
   * to correct the name if needed
   * to draw a square on the face
   * to click on a button to validate or reject the annotation (if there is no written name or pronounced name corresponding to the person name)
 
![OCR](OCR.png)

## Verification of face identities

#### Input data: 
 - Image of the face corresponding to an evidence (provide by the previous step)
 - List of shots

#### Scenario :
- Show the evidence on the left side
- Show a list of shot of video to be annoted on the right side
- Ask to the annotator for each shot selected:
   * To play the shot
   * To draw a square around the face corresponding to the evidence
   * Or to click on a button to reject the shot if the person don't appear

 ![Face](Face.png)

## Verification of speaking face

#### Input data: 
 - A shot of a video
 - A face selected (provide by the previous step)

#### Scenario :
- Show the shot of the video
- Draw a square on the face selected
- Ask to the annotator:
   * To play the shot
   * To click on a button to validate that is a speaking face or not 

 ![Speaking_face](Speaking_face.png)
