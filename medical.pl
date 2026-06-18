disease(fever,flu).
disease(cough,flu).
disease(headache,flu).

diagnosis(Symptom,Disease) :-
    disease(Symptom,Disease).