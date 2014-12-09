# Task proposal for MediaEval 2015

## Task description

### Task title

```
Give your task an informative title.
```

Multimodal person discovery in TV Broadcast

```
Unsupervised  | Person | Discovery | in TV Broadcast
Multi-modal   |        | Spotting  | 
Cross-modal   |        | Naming
```

### Introduction

```
Describe the motivating use scenario, i.e,. which application(s) motivate the task. 
State what the task requires of participants.
```

The REPERE challenge is an evaluation campaign on multimodal person recognition (phase 1 took place in January 2013 and phase 2 in January 2014). The main objective of this challenge is to answer the four following questions at any instant of the video: Who speaks? Who is seen? Whose name is pronounced? Whose name is written on screen? All modalities available (audio, image, external data, etc.) can be used for answering these questions

archivist/journalist ==> needs to be sure of the identity when choosing which picture to use

Different scenarios underlying the task can be proposed to user like archivist or journalist:
  
  * Navigate into a video: a user wants to retrieve when a person is present in a video and jump from a video segment to another.
  * Video search: a user wants to retrieve a set of video where a given person is present.

#### Main task

Given a collection of TV broadcasts pre-segmented into shots, participants are asked to provide, for each shot, the list of names of persons speaking AND appearing at the same time.

The main novelty is that the list of persons is not provided *a priori* and the use of pre-existing biometric models (either from voice or from face) is forbidden. The only way to identify a person is by finding their name in the audio (*e.g.* using automatic speech recognition) or visual (*e.g.* using optical character recognition) streams and associating them to the correct person - making the task completely unsupervised.

![Propagation](propagation.png)

Participants are also asked to provide a proof for every result they return.
A proof is a short temporal video fragment making it clear (from a human perspective) what the name of the person is. For instance, it can be a different shot where the same person is introduced by a text overlay containing their name (`proofSource = OCR`), the same shot where the person introduces themself (`proofSource = ASR`), or their Wikipedia page (`proofSource = wikipedia`).

```
shotVideo shotStartTime shotEndTime First-Name_LAST-NAME proofSource proofVideo proofStartTime proofEndTime
shotVideo shotStartTime shotEndTime First-Name_LAST-NAME wikipedia http://wikipedia.org/...
```
  * `shotVideo`:
  * `shotStartTime`: 
  * `shotEndTime`:
  * `First-Name_LAST-NAME`: 
  * `proofSource`: `ASR`, `OCR` or `Wikipedia`
  * `proofVideo`:
  * `proofStartTime`: 
  * `proofEndTime`:

#### Optional task

As we expect most submissions to internally rely on two-steps approaches (*i.e.* speaking-face diarization followed by propagation of detected names), an optional task is dedicated to the evaluation of underlying audio-visual diarization technologies.

In this optional task, participants are asked to provide a temporal segmentation of the whole test corpus containing every temporal fragment where at least one person is speaking and appearing at the same time. Moreover, each person should be uniquely identified by an anonymous label (*e.g.* `person1`, `person2`, ...)

```
video startTime endTime personLabel
```
  * `video`:
  * `startTime`: 
  * `endTime`:
  * `personLabel`:

### Target group

```
Describe the type of researchers who would be interested in participating in the task.
```

This task targets researchers from several communities including multimedia, computer vision, speech and natural language processing. Though the task is multimodal by design and necessitates expertise in various domains, the technological barriers to entry is lowered by the fact that the automatic output of various sub-modules will be provided to all participants:

  * speaker diarization,
  * face detection and tracking,
  * automatic speech transcription,
  * optical character recognition,
  * named entity detection

For instance, a researcher from the speech processing community could focus its research efforts on improving speaker diarization and automatic speech transcription, while still being able to rely on provided face detection and tracking results to participate to the task.

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

On these lists we will make requests (names, dates) depending on the popularity of the people in the Google trends. The query results will allow us to assess the quality of the indexation.
To evaluate the intrinsic diarization system quality we also propose a third subtask:

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

#### Paper by REPERE challenge 2013 organizers

G. Bernard, O. Galibert, J. Kahn  
*The First Official REPERE Evaluation*  
SLAM 2013, First Workshop on Speech, Language and Audio for Multimedia  
[PDF](http://ceur-ws.org/Vol-1012/papers/paper-08.pdf)

#### Paper by REPERE corpus creators

A. Giraudel, M. Carré, V. Mapelli, J. Kahn, O. Galibert, L. Quintard  
*The REPERE Corpus: a Multimodal Corpus for Person Recognition*  
LREC 2014, Eight International Conference on Language Resources and Evaluation  
[PDF](http://www.lrec-conf.org/proceedings/lrec2012/pdf/707_Paper.pdf)

#### Paper by REPERE challenge 2014 winning consortium

F. Bechet, M. Bendris, D. Charlet, G. Damnati, B. Favre, M. Rouvier, R. Auguste, B. Bigot, R. Dufour, C. Fredouille, G. Linarès, J. Martinet, G. Senay, P. Tirilly  
*Multimodal Understanding for Person Recognition in Video Broadcasts*  
InterSpeech 2014, Fifteenth Annual Conference of the International Speech Communication Association  
[PDF](http://pageperso.lif.univ-mrs.fr/~benoit.favre/papers/favre_interspeech2014b.pdf)

#### Papers by the organizers

H. Bredin, A. Laurent, A. Sarkar, V.-B. Le, S. Rosset, C. Barras  
*Person Instance Graphs for Named Speaker Identification in TV Broadcast*  
Odyssey 2014, The Speaker and Language Recognition Workshop  
[PDF](http://cs.uef.fi/odyssey2014/program/pdfs/27.pdf)

J. Poignant, L. Besacier, G. Quénot  
*Unsupervised Speaker Identification in TV Broadcast Based on Written Names*  
IEEE/ACM Transactions on Audio, Speech, and Language Processing  
[PDF](https://hal.archives-ouvertes.fr/hal-01060827/document)

### List of task organizers

  * Johann Poignant (LIMSI/CNRS)
  * Claude Barras (LIMSI/Université Paris-Sud)
  * Hervé Bredin (LIMSI/CNRS)
  * Juliette Kahn (LNE) ?
  * Sylvain Meignier (LIUM) ?
  
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

  * Johann Poignant, LIMSI, France
  * Hervé Bredin, LIMSI, France
  * Claude Barras, LIMSI, France
  * Juliette Kahn, LNE, France
  * LIG ???


## Survey questions
```
Write a list of questions (3-5) that you would like to include on the survey. 
These questions help you to ascertain the preferences of the research community for the aspects 
of the design of the task formulation, the data set design, and the evaluation methodology. 
For examples of the types of ￼questions asked by tasks, please have a look at this .pdf
for the MediaEval 2013 survey.
```

- What is your opinion about requests selected according to the Google trend.
  * Very interested.
  * Not interested

- Do you think that we should add requests for the anchors and journalists?
 * Yes
 * No

- The responses to the requests should be on persons:
 * Speaking AND appearing
 * Speaking OR appearing

- How much data do you needs for the development set (there is no training data, systems should be unsupervised)?
 * 5 hours
 * 10 hours
 * 20 hours

- How much time can you devote to the post-annotation to increase the number of requests evaluated:
 * 0 hours
 * 25 hours
 * 50 hours
 * 75 hours
 * 100 hours

- If any additional comments, questions or suggestions about this task occurred to you while you were answering the detailed questions, it would be helpful if you could enter them here:
