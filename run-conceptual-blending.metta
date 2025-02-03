 ;; Import the conceptual blending module for knowledge representation
! (import! &self conceptual_blending)

 ;; Ask the GPT agent with a general conceptual blending question
! (gpt "How does music relate to painting?")

 ;; Combine GPT with other agents and workflows
 ;; For example, Store the blended knowledge(GPT response) to the knowledge space
! (add-reduct &self (gpt "How does music relate to painting?"))

 ;; Retrieve and list all knowledge stored in the current space
! (match &self ($x) $x)
