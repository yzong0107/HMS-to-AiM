# Steps in ResCenter

1. Login, go to Facilities->Work Orders
2. Change status to "NEW"

![search](images/search.png)

3. Select the top record from the list.

![top record](images/select.png)

4. Read & store information

   ![res_info](images/store_res.png)

5. Log customer request into AiM

   ![aim](images/aim.png)

   ![aim CR no](images/aim_CR_no.png)

6. update ResCenter records, description -> “AiM CR ##### - ”original description

   ![res_update](images/res_update.png)

7. Wait until the success alert pops up, then close it and go back to the search page.

   ![res_save](images/res_saved.png)

8. Go to the next record, and proceed.

   ![res next](images/res_next.png)



# Exceptions

1. If WO type is either "Contractor" or "Pest Control", then this record **won't** be logged into AiM, and status will be changed to "**Pending ASIWC Approval**".

2. In some cases, the mandatory location field is missing, capture the error.

   ![exception1](images/res_exception1.png)

   change status to "Pending ASIWC Approval", auto fill location to "ASIWC Office"

   ![exception2](images/res_exception2.png)

   