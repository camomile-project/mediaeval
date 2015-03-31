mediaeval data
==============

# Package REPERE (FTP or HD)
 - ELDA_package

# GitHub.com/PersonDiscoveryatMediaeval2015 

## Task
 - Proposal.md

## Metric
 - Reference_shot.ref
 - Reference_evidence.ref
 - Hypothesis_baseline1.hyp
 - Hypothesis_baseline2.hyp
 - eval_MMAP.py
 - eval_evidence.py
 - Global_eval.py
 - uri_list
   + mapping_uri_to_media
   + uri.train1.lst
   + uri.train2.lst
   + uri.dev1.lst
   + uri.dev2.lst
   + uri.test1.lst
   + uri.test2.lst
 
## Metadata : automatic_annotation_on_raw_video
 - Shot_segmentation
 - Video_OCR
 - ASR
 - Spoken_name
 - SpeechTurn_segmentation
 - Speaker_diarization
 - Face_segmentation
 - SpeakingFace_segmentation
 - Face_clustering
 - SpeakingFace_clustering
 - SpeechTurn_Face_clustering
 - SpeechTurn_SpeakingFace_clustering
 - Distance_SpeechTurn_vs_SpeechTurn
 - Distance_Face_vs_Face
 - Distance_SpeakingFace_vs_SpeakingFace
 - Distance_SpeechTurn_vs_SpeakingFace
 - Fusion_baseline1
 - Fusion_baseline2

## Source code automatic system
 - README.md
 - Fusion_baseline_system
   + Fusion_baseline1.py
   + Fusion_baseline2.py
 - sub-component
   + 1_Shot
     * 1_extract_descriptor.py
     * 2_segmentation.py
   + 2_SpeechTurn
     * 1_learn_model_speech_nonspeech.py
     * 2_speech_nonspeech_segmentation.py
     * 3_speech_turn_segmentation.py
     * 4_linear_clustering.py
     * 5_Compute_BIC_distance.py
     * 6_learn_model_normalisation.py
     * 7_Compute_matrix_distance_SpeechTurn_vs_SpeechTurn.py  
   + 3_Face
     * 1_detection.py
     * 2_tracking.py
     * 3_extract_flandmark
       - landmarks_detection.cpp
       - CMakeLists.txt
       - libflandmark
         + flandmark_detector.cpp
         + flandmark_detector.h
         + liblbp.cpp
         + liblbp.h
         + msvc-compat.h
         + CMakeLists.txt
     * 4_extract_HoG_descriptor.py
     * 5_project_HOG_descriptor_by_LDML.py
     * 6_learn_model_normalisation.py
     * 7_Compute_matrix_distance_Face_vs_Face.py
   + 4_SpeakingFace
     * 1_extract_descriptor_of_SpeakingFace.py
     * 2_learn_model_for_selection_of_SpeakingFace.py
     * 3_select_SpeakingFace.py
     * 4_extract_descriptor_SpeechTurn_vs_SpeakingFace.py
     * 5_learn_model_distance_SpeechTurn_vs_SpeakingFace.py
     * 6_Compute_matrix_distance_SpeechTurn_vs_SpeakingFace.py
   + 5_OverlaidName
     * 1_LOOV
     * 2_merge_multiple_transcriptions.py
     * 3_extract_OverlaidName_segmentation.py
   + 6_evaluation
     * eval_speech_nonspeech_segmentation.py
     * eval_speech_turn_segmentation.py
     * align_speechTurn_to_reference.py
     * eval_face_detection.py
     * eval_facetracks.py
     * align_faceTracks_to_reference.py
     * eval_matrix_distance.py
   + Model
     * Speech_nonspeech.model
     * Normalisation_BIC_distance.model
     * haarcascade_frontalface_default.xml
     * flandmark_model.dat
     * LDML.model
     * Normalisation_l2_distance.model
     * SpeakingFace_selection.model
     * SpeechTurn_vs_SpeakingFace_distance.model
     * Model_title_box_BFMSTORY1.png
     * Model_title_box_BFMSTORY2.png
     * Model_title_box_...
     * Model_title_box_INA1.png 
   



