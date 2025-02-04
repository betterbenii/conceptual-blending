 ;; Import the conceptual blending module for knowledge representation
! (import! &self conceptual_blending)

 ;; Ask the GPT agent with a general conceptual blending question
 ; ! (gpt "How does music relate to painting?")
 ; ! (gpt "How is AI related to Psychology?")

 ;  ;; Combine GPT with other agents and workflows
 ;  ;; For example, Store the blended knowledge(GPT response) to the knowledge space
 ; ! (add-reduct &self (gpt "How does music relate to painting?"))
 ; ! (add-reduct &self (gpt "How is AI related to Psychology?"))

 ;  ;; Retrieve and list all knowledge stored in the current space
 ; ! (match &self ($x) $x)

 ; Test queries

 ; ! (gpt "How does AI relate to Psychology?")
 ; ! (gpt "How does electricity relate to water flow?")
 ; ! (gpt "How does language relate to mathematics?")

 ; ! (gpt "How does thunder relate to a speaker?")
 ; ! (gpt "How does a river relate to a road?")
 ; ! (gpt "How does a clock relate to a calendar?")

 ; ! (gpt "How does drug manufacturing relate to speech?")
 ; ! (gpt "How does software engineering relate to construction?")
 ; ! (gpt "How does genetics relate to programming?")

! (gpt "How does theater management relate to political dictatorship?")
! (gpt "How does cooking relate to chemistry?")
! (gpt "How does war strategy relate to video games?")
