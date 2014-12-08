# Task proposal for MediaEval 2015

## Task description

### Task title

```
Give your task an informative title.
```

Multimodal person discovery in TV broadcast

### Introduction

```
Describe the motivating use scenario, i.e,. which application(s) motivate the task. 
State what the task requires of participants.
```

The REPERE challenge is an evaluation campaign on multimodal person recognition (phase 1 took place in January 2013 and phase 2 in January 2014). The main objective of this challenge is to answer the four following questions at any instant of the video: Who speaks? Who is seen? Whose name is pronounced? Whose name is written on screen? All modalities available (audio, image, external data, etc.) can be used for answering these questions


To extend this challenge we propose a more applicative task. This task is based on a classical framework: return a list of shot where a person is speaking and appearing at the same time. Which we add an original dimension: no a priori knowledge on persons present in these videos. This implies the need to find the identity of person within a modality of the videos. This novelty leads us to the first subtask:

#### Subtask1: Find a proof of the identities the persons

A proof can be a shot where we can see the person speaking and his name written on screen, or a sequence where a person speak and appears and with his name is pronounced just before or after.
From these proofs, the participants are asked to provide a list of shots where people appear and speak at the same time (to force the multi-modality of the process). This is the core of the proposed task:

#### Subtask2: unsupervised multimodal person indexing

On these lists we will make requests (names, dates) depending on the popularity of the people in the Google trends. The query results will allow us to assess the quality of the indexation.
To evaluate the intrinsic diarization system quality we also propose a third subtask:

#### Subtask3: Multimodal person diarization (AV)

Where the expected results are a multimodal anonymous segmentation with identical tags for face and speech segment of a person.

### Target group

```
Describe the type of researchers who would be interested in participating in the task.
```

Different scenarios underlying the task can be proposed to user like archivist or journalist:
  
  * Navigate into a video: a user wants to retrieve when a person is present in a video and jump from a video segment to another.
  * Video search: a user wants to retrieve a set of video where a given person is present.

### Data

```
Describe the data set, including how the data will be collected an licensed.
```

The REPERE data set (137 hours) will be dividing into two parts: a development set used to tune the fusion system and a test set. We split the corpus to have the minimum overlap between persons present in the two subsets, which will avoid the use of biometric models.
50 hours are already manually annotated:

  * Audio: speech transcript, named entities, speech segmentation, speech identification
  * Image (1/10 seconds): face segmentation and identification, overlaid text transcription, mark on person name in overlaid text,
  * Complete face tracking on 10 hours

To complete these annotations for the two first subtasks, a posteriori annotation interface build for the CAMOMILE project will be used.

### Evaluation methodology

```
Describe the evaluation methodology, including how the ground truth will be created.
```

A posteriori shot annotation depending on what is return by participants. Metrics are the classical precision recall and F1-measure. These metrics are compute for each request. The global score corresponding to the mean score

  * P(request/video) = # correct shots / # hypothesis shot
  * R(request/video) = # correct shots / # shot in the reference

where “#shot in the reference” is not exhaustive, it corresponds to the shot annotated a posteriori. More a participant return good shot, more the task is hard for the other participants.
For the diarization task, we will use the diarization error rate (DER) classically used in the speech community.
We will also propose an on line adjudication interface to solve ambiguous cases.


### References and recommended reading

```
List 3-4 references related to the task that teams should have read before attempting the task.
```

  * G. Bernard, O. Galibert, J. Kahn The Second Official REPERE Evaluation SLAM 2014, Second Workshop on Speech, Language and Audio for Multimedia
  * F. Bechet, M. Bendris, D. Charlet, G. Damnati, B. Favre, M. Rouvier, R. Auguste, B. Bigot, R. Dufour, C. Fredouille, G. Linarès, J. Martinet, G. Senay, P., T. Multimodal understanding for person recognition in video broadcasts InterSpeech 2014, Fifteenth Annual Conference of the International Speech Communication Association
  * A. G., M. Carré, V. Mapelli, J. Kahn, O. Galibert, L. Quintard, The REPERE Corpus: a multimodal corpus for person recognition. LREC 2012

### List of task organizers

  * Johann Poignant
  * Claude Barras
  * Hervé Bredin 
  
(firstname.lastname@limsi.fr)

## Task blurb

```
￼Write 2-3 sentences that summarizes key information on the task.
It should be informative and well- crafted to attract potential participants. 
A standard pattern is to have each sentence answer in turn the major questions about the task: 
First sentence: What is the input and the output of the algorithm that participants need to design for the task?
Second sentence: What is the data? 
Third sentence: How is the ￼task evaluated?
```

## Task organization team

```
Write a short paragraph describing the organizing team. 
Your team should be large enough to handle organizing the task. 
Teams should consists of members from multiple research sites and multiple projects. 
A mix of experienced and early-career researchers is recommended. 
Note that your task team ￼can add members after the proposal has been accepted.
```

## Survey questions

```
Write a list of questions (3-5) that you would like to include on the survey. 
These questions help you to ascertain the preferences of the research community for the aspects 
of the design of the task formulation, the data set design, and the evaluation methodology. 
For examples of the types of ￼questions asked by tasks, please have a look at this .pdf
for the MediaEval 2013 survey.
```
