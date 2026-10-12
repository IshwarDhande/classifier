# Response File Guide

This guide provides an overview and logical categorization of all the core "response" related documents. The directory has been cleaned and reorganized into a sequential flow (from 01 to 14) following the model's design, architecture, logic, and specific categorizations.

## Sequential File Structure

+-------------------------------------------------------------+
|                     Response Architecture                   |
+-------------------------------------------------------------+
|                                                             |
|  [01-03] Architecture & Design Overview                     |
|    |-- 01_user_response_design_process.md                   |
|    |-- 02_user_response_model.md                            |
|    |-- 03_response_category_ontology.md                     |
|                                                             |
|  [04-06] Core Model Components                              |
|    |-- 04_user_response_appraisal_model.md                  |
|    |-- 05_user_response_mapping_model.md                    |
|    |-- 06_response_model_calibration.md                     |
|                                                             |
|  [07-09] Reference & Logic Rules                            |
|    |-- 07_response_reference_values.md                      |
|    |-- 08_response_decision_tree.md                         |
|    |-- 09_response_annotation.md                            |
|                                                             |
|  [10-14] Category Definitions                               |
|    |-- 10_response_vp.md (Very Positive)                    |
|    |-- 11_response_p.md (Positive)                          |
|    |-- 12_response_i.md (Indifferent)                       |
|    |-- 13_response_n.md (Negative)                          |
|    |-- 14_response_vn.md (Very Negative)                    |
|                                                             |
+-------------------------------------------------------------+

## 1. Architecture & Design Overview (`01` to `03`)
These documents provide the highest level of abstraction, documenting the conceptual design process, the overall user response model, and the formal ontology of categories.

* `01_user_response_design_process.md`: The high-level workflow and design process.
* `02_user_response_model.md`: The core master document outlining the user response model architecture.
* `03_response_category_ontology.md`: The formalized ontology and overarching summary of response categories.

## 2. Core Model Components (`04` to `06`)
These files detail the specific mathematical and conceptual models that sit inside the overall architecture, focusing on appraisal, mapping, and calibration.

* `04_user_response_appraisal_model.md`: The appraisal function mapping.
* `05_user_response_mapping_model.md`: The mapping mechanics.
* `06_response_model_calibration.md`: Details and plans on model calibration.

## 3. Reference & Logic Rules (`07` to `09`)
These documents cover the numeric thresholds, branching logic workflows, and annotation schemas used in practice by the interpreter.

* `07_response_reference_values.md`: The strict numeric bounds and reference values for the response ontology.
* `08_response_decision_tree.md`: The logic tree mapping responses to downstream outcomes.
* `09_response_annotation.md`: Semantic state annotation rules.

## 4. Category Definitions (`10` to `14`)
This set of files acts as the single source of truth for the interpretation and formal definition of each specific response level.

* `10_response_vp.md`: Very Positive (VP)
* `11_response_p.md`: Positive (P)
* `12_response_i.md`: Indifferent (I)
* `13_response_n.md`: Negative (N)
* `14_response_vn.md`: Very Negative (VN)
