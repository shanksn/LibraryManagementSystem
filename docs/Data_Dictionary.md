# Field-level Data Dictionary (table format)

Below are the tables and **field-by-field descriptions** you requested. Each table is presented as a bordered table (Markdown).
**Important note:** ID columns that are **system-generated** (e.g., `id`, auto-increment keys) **may be omitted** by the vendor if they do not convey relationship mapping or business meaning. If you need relational mapping, request the vendor include IDs and any foreign-key-like columns (e.g., `applicant_id`, `chit_id`, `ticket_no`). Also request **full historical data (from system inception to date) as CSVs**.

---

## Employee

| Field           | Description                                     | Note                                                 |
| --------------- | ----------------------------------------------- | ---------------------------------------------------- |
| branch          | Branch/office where the employee is assigned.   |                                                      |
| full_name       | Employee’s complete legal name.                 |                                                      |
| salutation      | Prefix (Mr./Ms./Dr.).                           |                                                      |
| dob             | Date of birth.                                  |                                                      |
| gender          | Gender of the employee.                         |                                                      |
| marital_status  | Marital status (Single/Married).                |                                                      |
| father_name     | Father's name.                                  |                                                      |
| spouse_name     | Spouse's name (if any).                         |                                                      |
| date_of_joining | Date employee joined.                           |                                                      |
| designation     | Job title / role.                               |                                                      |
| department      | Department name (HR/Finance/etc).               |                                                      |
| city            | City of residence.                              |                                                      |
| emp_rights      | System/application access rights or privileges. |                                                      |
| address         | Full residential address.                       |                                                      |
| state           | State of residence.                             |                                                      |
| country         | Country of residence.                           |                                                      |
| pincode         | Postal / ZIP code.                              |                                                      |
| mobile_no       | Primary mobile number.                          |                                                      |
| email           | Work / personal email address.                  |                                                      |
| emp_status      | Employment status (Active/Resigned).            |                                                      |
| ref_code        | Internal employee code / reference.             | If vendor has their own employee ID include mapping. |

---

## Application (applicant / customer master)

| Field                    |                                                   Description | Note                                              |
| ------------------------ | ------------------------------------------------------------: | ------------------------------------------------- |
| branch                   |                           Branch where application submitted. |                                                   |
| applicant_id             |                         Unique applicant identifier (vendor). | Include if available for mapping.                 |
| customer_type            |                                New or existing customer flag. |                                                   |
| salutation               |                                               Prefix (Mr/Ms). |                                                   |
| gender                   |                                                       Gender. |                                                   |
| full_name                |                                          Applicant full name. |                                                   |
| chit_id                  |                    Chit/group identifier the applicant joins. | Include for mapping membership.                   |
| ticket_no                |                          Ticket number assigned within group. | Important for membership history.                 |
| dob                      |                                                Date of birth. |                                                   |
| marital_status           |                                               Marital status. |                                                   |
| spouse_name              |                                                  Spouse name. |                                                   |
| father_name              |                                                Father's name. |                                                   |
| occupation               |                                 Job / occupation description. |                                                   |
| source_income            |                                        Primary income source. |                                                   |
| monthly_income           |                                        Monthly income amount. |                                                   |
| other_income             |                                         Other income streams. |                                                   |
| address                  |                                          Residential address. |                                                   |
| city                     |                                                         City. |                                                   |
| pincode                  |                                                  Postal code. |                                                   |
| state                    |                                                        State. |                                                   |
| country                  |                                                      Country. |                                                   |
| mobile_no                |                                               Primary mobile. |                                                   |
| alt_mobile_no            |                                             Alternate mobile. |                                                   |
| email                    |                                                Email address. |                                                   |
| nominee_name             |                                    Nominee name for the chit. |                                                   |
| nominee_relation         |                             Relation of nominee to applicant. |                                                   |
| nominee_contact          |                                         Nominee phone number. |                                                   |
| nominee_address          |                                              Nominee address. |                                                   |
| ref_code                 |                         Reference code (introducer/referrer). |                                                   |
| introducer_type          |                          Type of introducer (agent/customer). |                                                   |
| agent_name               |                                          Agent name (if any). |                                                   |
| agent_commission         |                                Commission allocated to agent. |                                                   |
| employee_name            |                                   Staff handling application. |                                                   |
| employee_share           |                                    Employee commission/share. |                                                   |
| surety_type              |                             Type of surety/guarantee offered. |                                                   |
| property_type            |          If property surety — property type (house/gold/etc). |                                                   |
| property_value           |                           Estimated value of property surety. |                                                   |
| undertaking_months       |                               Period of undertaking validity. |                                                   |
| personal_surety_type     |               Type of personal guarantor (salary/individual). |                                                   |
| personal_surety_value    |                            Value assigned to personal surety. |                                                   |
| surety_future_due        |                     Future dues/obligations linked to surety. |                                                   |
| surety_chit_id           |                     If surety uses another chit, its chit_id. |                                                   |
| surety_lot_no            |                    Lot number used as surety (if applicable). |                                                   |
| other_surety_type        |                            Any other surety type description. |                                                   |
| surety_attachment        |              File path / name of documents supporting surety. | Ask for document filenames and storage reference. |
| surety_comment           |                      Staff remarks about surety verification. |                                                   |
| canvasser_comment        |                                Field staff / canvasser notes. |                                                   |
| app_first_approval       |                               First-level approval indicator. |                                                   |
| app_final_approval       |                                     Final approval indicator. |                                                   |
| reconsider_app           |                                         Reconsideration flag. |                                                   |
| reconsider_reason        |                                   Reason for reconsideration. |                                                   |
| reject_app               |                                               Rejection flag. |                                                   |
| reject_reason            |                                         Reason for rejection. |                                                   |
| created_by               |                                  User who created the record. |                                                   |
| updated_by               |                             Last user who updated the record. |                                                   |
| is_first_ins_paid        |                           Whether first installment was paid. |                                                   |
| is_auction_winner        |                             Flag if applicant won an auction. |                                                   |
| app_status               |               Application status (Pending/Approved/Rejected). |                                                   |
| family_id                |                         Family grouping identifier (if used). |                                                   |
| group_fee_amt            |                                     Group joining fee amount. |                                                   |
| group_gst_amt            |                                      GST amount on group fee. |                                                   |
| group_sgst_amt           |                                                 SGST portion. |                                                   |
| group_cgst_amt           |                                                 CGST portion. |                                                   |
| transfer_fee_amt         |                                      Fee for ticket transfer. |                                                   |
| transfer_gst_amt         |                                          GST on transfer fee. |                                                   |
| transfer_sgst_amt        |                                         SGST on transfer fee. |                                                   |
| transfer_cgst_amt        |                                         CGST on transfer fee. |                                                   |
| is_main                  |                      If customer is the primary holder (Y/N). |                                                   |
| personal_photo           |                              Filename/path to personal photo. | Request file storage details.                     |
| aadhar_card              |                           Filename/path to Aadhaar image/pdf. |                                                   |
| pan_card                 |                               Filename/path to PAN image/pdf. |                                                   |
| bank_passbook            |                         Filename/path to bank passbook image. |                                                   |
| driving_license          |                                     Driving license doc path. |                                                   |
| voter_id                 |                                            Voter id doc path. |                                                   |
| smart_card               |                                          Smart card doc path. |                                                   |
| signature                |                                Captured signature image path. |                                                   |
| passport                 |                                            Passport doc path. |                                                   |
| createdAt                |                                           Creation timestamp. |                                                   |
| updatedAt                |                                        Last update timestamp. |                                                   |
| replacement_for_transfer | If this row replaced someone during transfer — ID/identifier. |                                                   |
| no_of_guarantee          |                                Number of guarantees provided. |                                                   |
| annual_salary            |                                  Annual salary (if provided). |                                                   |
| surety_address           |                                  Address of surety/guarantor. |                                                   |
| employee_type            |                   Applicant employee type (if employee chit). |                                                   |
| removed_member           |                                Flag if applicant was removed. |                                                   |
| transfer_by              |                                       Who initiated transfer. |                                                   |
| transfered_member        |                              Member id who received transfer. |                                                   |
| consent_letter           |                              Filename/path of consent letter. |                                                   |
| md_consent               |                                        MD level consent flag. |                                                   |
| consent_status           |                                      Consent workflow status. |                                                   |
| is_consent_approved      |                                  Boolean if consent approved. |                                                   |
| notice_charge_value      |                                   Notice legal charge amount. |                                                   |
| suit_charge_values       |                 Suit/legal charge amount JSON or multi-field. | Ask for JSON keys if present.                     |
| igst_amt                 |                                  IGST amount (if applicable). |                                                   |
| is_igst                  |                                         Flag if IGST applied. |                                                   |

---

## Group

| Field               | Description                              | Note                                           |
| ------------------- | ---------------------------------------- | ---------------------------------------------- |
| branch              | Branch creating the chit group.          |                                                |
| chit_id             | Unique chit/group identifier.            | Important for mapping; request vendor chit_id. |
| amount              | Total chit amount (face value).          |                                                |
| duration_type       | Unit for duration (Months/Weeks).        |                                                |
| member              | Number of members in group.              |                                                |
| duration            | Number of periods (eg months).           |                                                |
| is_group_fee        | Whether group joining fee is applicable. |                                                |
| is_transferfee      | Whether transfer fee applies.            |                                                |
| group_fee_amt       | Fee amount for joining.                  |                                                |
| group_gst_amt       | GST on group fee.                        |                                                |
| group_sgst_amt      | SGST portion.                            |                                                |
| group_cgst_amt      | CGST portion.                            |                                                |
| transfer_fee_amt    | Transfer fee amount.                     |                                                |
| transfer_gst_amt    | GST on transfer fee.                     |                                                |
| transfer_sgst_amt   | SGST on transfer fee.                    |                                                |
| transfer_cgst_amt   | CGST on transfer fee.                    |                                                |
| commencement_date   | Group start date.                        |                                                |
| termination_date    | Group end date.                          |                                                |
| bid_range           | Allowed bid/discount range (policy).     |                                                |
| first_auction_date  | Date of first auction.                   |                                                |
| auction_start_time  | Auction start time.                      |                                                |
| auction_end_time    | Auction end time.                        |                                                |
| active_status       | Whether group is active.                 |                                                |
| is_admin_decision   | Whether admin intervention happened.     |                                                |
| approved_status     | Approval status of group.                |                                                |
| admin_decision_date | Date admin made decision.                |                                                |
| created_date        | Group record creation date.              |                                                |
| created_by          | Creator user.                            |                                                |
| updated_tax         | Updated tax configuration if changed.    |                                                |
| monthly_due         | Monthly installment per member.          |                                                |
| updated_by          | Last updater.                            |                                                |
| is_employee_chit    | Indicates special employee chit.         |                                                |

---

## Auction (auction list)

| Field          | Description                                   | Note |
| -------------- | --------------------------------------------- | ---- |
| chit_id        | Chit/group id for auction.                    |      |
| auction_no     | Sequence number of auction in cycle.          |      |
| auction_date   | Date auction was held.                        |      |
| auction_status | Auction status (Completed/Scheduled).         |      |
| auction_winner | Winner applicant_id or ticket_no.             |      |
| prize_amount   | Amount awarded to winner after bid deduction. |      |
| ins_dividend   | Dividend amount distributed to members.       |      |
| bid_amount     | Bid/discount amount offered by winner.        |      |

---

## Auction Winner

| Field               | Description                                          | Note                                  |
| ------------------- | ---------------------------------------------------- | ------------------------------------- |
| applicant_id        | ID of auction winner.                                | Include for mapping payments/history. |
| full_name           | Winner name.                                         |                                       |
| chit_id             | Chit id.                                             |                                       |
| ticket_no           | Ticket number.                                       |                                       |
| auction_no          | Auction number.                                      |                                       |
| auction_date        | Auction date.                                        |                                       |
| chit_amount         | Chit face amount.                                    |                                       |
| bid_amount          | Bid offered by winner.                               |                                       |
| prize_amount        | Winner payout amount.                                |                                       |
| company_commission  | Company commission for that auction.                 |                                       |
| total_dividend      | Total dividend sum to be shared.                     |                                       |
| net_dividend        | Dividend after deductions.                           |                                       |
| dividend_per_person | Per-member dividend.                                 |                                       |
| ins_due             | Installment amount due for winner after adjustments. |                                       |
| winner_status       | Winner record status.                                |                                       |
| createdAt           | Record creation timestamp.                           |                                       |
| updatedAt           | Last update timestamp.                               |                                       |

---

## Auction Reject

| Field         | Description                    | Note                                 |
| ------------- | ------------------------------ | ------------------------------------ |
| reject_id     | Rejection record id (system).  | System ID may be optional.           |
| applicant_id  | Applicant id rejected.         | Required to trace applicant history. |
| full_name     | Applicant name.                |                                      |
| chit_id       | Chit id.                       |                                      |
| ticket_no     | Ticket number.                 |                                      |
| auction_no    | Auction number of rejection.   |                                      |
| chit_amount   | Chit value.                    |                                      |
| bid_amount    | Bid attempted.                 |                                      |
| createdAt     | Rejection timestamp.           |                                      |
| updatedAt     | Last updated timestamp.        |                                      |
| reject_reason | Reason recorded for rejection. |                                      |

---

## Auction Participant

| Field          | Description                           | Note                                                  |
| -------------- | ------------------------------------- | ----------------------------------------------------- |
| participant_id | Participant record id (system).       | Optional if vendor provides applicant/ticket mapping. |
| applicant_id   | Applicant id of participant.          | Important for mapping.                                |
| ticket_no      | Ticket number.                        |                                                       |
| full_name      | Participant name.                     |                                                       |
| chit_id        | Chit id.                              |                                                       |
| auction_no     | Auction number.                       |                                                       |
| auction_date   | Auction date.                         |                                                       |
| branch         | Branch where participation recorded.  |                                                       |
| amount         | Chit or bidding amount context.       |                                                       |
| max_bid_amount | Maximum allowed bid for participant.  |                                                       |
| min_bid_amount | Minimum allowed bid.                  |                                                       |
| bid_amount     | Actual bid placed.                    |                                                       |
| prize_amount   | Prize if participant wins.            |                                                       |
| is_winner      | Flag whether this participant won.    |                                                       |
| is_rejected    | Flag whether participant rejected.    |                                                       |
| is_by_lot      | Flag indicating winner chosen by lot. |                                                       |
| createdAt      | Record created timestamp.             |                                                       |
| updatedAt      | Record updated timestamp.             |                                                       |

---

## Installment

| Field                 | Description                                      | Note                                     |
| --------------------- | ------------------------------------------------ | ---------------------------------------- |
| id                    | Installment record id (system).                  | Optional unless used for reconciliation. |
| applicant_id          | Member/applicant paying installment.             | Required for payment history mapping.    |
| ins_no                | Installment sequence number.                     | Required.                                |
| ins_actual_due        | Original EMI before adjustments.                 |                                          |
| ins_due               | Final payable amount after dividend/adjustments. |                                          |
| ins_due_date          | Due date for the installment.                    |                                          |
| ins_dividend          | Dividend component adjusting the due.            |                                          |
| is_ins_paid           | Boolean paid flag.                               |                                          |
| ins_paid              | Amount actually paid.                            |                                          |
| ins_paid_date         | Date payment realized.                           |                                          |
| ins_status            | Payment status (Paid/Overdue).                   |                                          |
| ins_approval_status   | Approval workflow status.                        |                                          |
| ins_final_approval    | Final approval flag.                             |                                          |
| ins_reconsider        | Reconsideration flag.                            |                                          |
| ins_reconsider_reason | Reason for reconsideration.                      |                                          |
| ins_reject            | Rejection flag for payment record.               |                                          |
| ins_reject_reason     | Rejection reason.                                |                                          |
| chit_id               | Chit id.                                         |                                          |
| ticket_no             | Ticket number.                                   |                                          |
| createdAt             | Creation timestamp.                              |                                          |
| updatedAt             | Last update timestamp.                           |                                          |
| branch                | Branch where payment recorded.                   |                                          |
| full_name             | Denormalized applicant name.                     |                                          |
| amount_type           | Category of payment (Installment/Charge).        |                                          |
| charge_type           | Specific charge type if applicable.              |                                          |
| mode_of_payment       | Cash/Cheque/NEFT/UPI etc.                        |                                          |
| payment_type          | Sub-type (Full/Partial).                         |                                          |
| cashier_comment       | Cashier notes.                                   |                                          |
| cashier_executive     | Cashier name or code.                            |                                          |
| ins_first_approval    | First approval flag.                             |                                          |
| ins_approval          | Approval indicator.                              |                                          |
| excess_amount         | Excess paid amount if any.                       |                                          |
| receipt_no            | Payment receipt number.                          | Ask vendor for unique sample values.     |

---

## Group Registration Deposit

| Field                    | Description                                   | Note                                |
| ------------------------ | --------------------------------------------- | ----------------------------------- |
| id                       | Deposit record id (system).                   | Optional.                           |
| group_id                 | FK to group / chit.                           | Required to map deposits to groups. |
| pso_no                   | PSO (Police Standing Order) reference number. |                                     |
| pso_date                 | Date PSO issued.                              |                                     |
| registration_no          | Official registration number.                 |                                     |
| registration_date        | Registration date.                            |                                     |
| deposit_bank_id          | Bank identifier (vendor).                     |                                     |
| account_no               | Account number where deposit placed.          |                                     |
| deposit_type             | Type of instrument (FD/RD/Term).              |                                     |
| deposit_number           | Instrument number / reference.                |                                     |
| deposit_date             | Date deposit created.                         |                                     |
| maturity_date            | Maturity date.                                |                                     |
| interest_percentage      | Interest rate.                                |                                     |
| interest_mode            | Mode of interest payout.                      |                                     |
| maturity_amount          | Maturity amount expected.                     |                                     |
| created_date             | Record creation date.                         |                                     |
| created_by               | Creator user.                                 |                                     |
| nearest_police_station   | Police station for registration.              |                                     |
| registration_office_name | Registration office name.                     |                                     |
| weekly_holiday           | Weekly holiday of group (for scheduling).     |                                     |
| foreman_name             | Foreman / group lead name.                    |                                     |
| pso_doc                  | PSO document file path/name.                  | Request actual files or paths.      |
| registration_doc         | Registration document path/name.              |                                     |

---

## Removal

| Field                  | Description                           | Note                               |
| ---------------------- | ------------------------------------- | ---------------------------------- |
| id                     | Removal record id (system).           | Optional.                          |
| applicant_id           | Member id removed.                    | Required to trace removal history. |
| chit_id                | Group id.                             |                                    |
| full_name              | Member name.                          |                                    |
| ticket_no              | Ticket number.                        |                                    |
| amount                 | Chit / amount context.                |                                    |
| received_amount        | Amount already collected from member. |                                    |
| remaining_amount       | Outstanding amount at removal.        |                                    |
| duration               | Duration or remaining periods.        |                                    |
| latest_paid_insNo      | Latest installment number paid.       |                                    |
| removal_date           | Date removal executed.                |                                    |
| removal_first_approval | First approval flag/id.               |                                    |
| removal_final_approval | Final approval flag/id.               |                                    |
| removal_status         | Removal workflow status.              |                                    |
| removal_reason         | Reason for removal.                   |                                    |
| is_removed_member      | Boolean final removed flag.           |                                    |
| created_by             | Creator user.                         |                                    |
| updated_by             | Last updater.                         |                                    |
| createdAt              | Creation timestamp.                   |                                    |
| updatedAt              | Update timestamp.                     |                                    |

---

## Banking

| Field             | Description                             | Note      |
| ----------------- | --------------------------------------- | --------- |
| id                | Banking record id (system).             | Optional. |
| branch            | Branch associated with account/deposit. |           |
| chit_id           | Group id for which bank account used.   |           |
| account_no        | Bank account number.                    |           |
| deposit_type      | Type of account or deposit.             |           |
| address           | Bank branch address.                    |           |
| banking_status    | Active/Closed/Inactive state.           |           |
| created_by        | Creator user.                           |           |
| updated_by        | Last updater.                           |           |
| deposit_amount    | Deposit amount.                         |           |
| deposit_date      | Date of deposit.                        |           |
| maturity_date     | Maturity date of deposit.               |           |
| interest          | Interest rate or amount.                |           |
| interest_mode     | Payment mode for interest.              |           |
| cheque_issue_from | Cheque series / source reference.       |           |
| deposit_bank_name | Bank name.                              |           |

---

## Individual Charges

| Field                 | Description                                                       | Note                               |
| --------------------- | ----------------------------------------------------------------- | ---------------------------------- |
| id                    | Individual charge record id (system).                             | Optional.                          |
| chit_id               | Group id.                                                         |                                    |
| ticket_no             | Ticket number.                                                    |                                    |
| amount_type           | Category (Charges/Adjustment).                                    |                                    |
| charge_type           | Specific charge label (Suit/Notice).                              |                                    |
| charge_values         | JSON or structured breakdown (basic_amt, gst, sgst, cgst, total). | Ask vendor to provide sample JSON. |
| indiv_charge_status   | Human readable status of charge.                                  |                                    |
| is_indiv_charge_paid  | Boolean paid flag.                                                |                                    |
| charge_paid_date      | Date payment realized.                                            |                                    |
| indiv_charge_approval | Approval metadata/flag.                                           |                                    |
| payment_type          | Payment classification.                                           |                                    |
| remaining_duration    | Remaining installments (if charge relates to instalment).         |                                    |
| fututre_dues          | Projected future dues (typo preserved as in sheet).               |                                    |
| interest              | Interest amount or rate applied.                                  |                                    |
| interest_per_day      | Per-day interest used for fines.                                  |                                    |
| total_interest        | Total interest computed.                                          |                                    |
| diminustion_days      | Days used in diminution calculations.                             |                                    |
| net_due               | Net due after adjustments.                                        |                                    |
| court_name            | Court name if matter escalated.                                   |                                    |
| lawyer_name           | Assigned lawyer.                                                  |                                    |
| filing_date           | Date suit/notice filed.                                           |                                    |
| suit_status           | Current legal status.                                             |                                    |
| notes                 | Free text notes.                                                  |                                    |
| createdAt             | Created timestamp.                                                |                                    |
| updatedAt             | Updated timestamp.                                                |                                    |
| applicant_id          | Applicant foreign key.                                            |                                    |
| mode_of_payment       | Cheque/Cash/UPI etc.                                              |                                    |
| cashier_comment       | Cashier notes on payment.                                         |                                    |
| cashier_executive     | Name/id of cashier.                                               |                                    |
| receipt_no            | Receipt or voucher number.                                        |                                    |
| full_name             | Denormalized member name for reporting.                           |                                    |
| charge_amount         | Numeric summary of charge.                                        |                                    |

---

## Payment

| Field                     | Description                                                     | Note                           |
| ------------------------- | --------------------------------------------------------------- | ------------------------------ |
| applicant_id              | Applicant id (FK).                                              | Required for mapping payments. |
| final_surety_type         | Type of final surety selected.                                  |                                |
| property_security_value   | JSON/object with property surety details and registration info. | Request sample JSON.           |
| undertaking_values        | Values related to undertakings pledged by applicant.            |                                |
| personal_surety_type      | Type of personal surety.                                        |                                |
| personal_surety_value     | Value of personal surety.                                       |                                |
| chit_undertaking_value    | Undertaking specific to chit obligations.                       |                                |
| full_settlement_value     | Full settlement amount if any.                                  |                                |
| final_settlement_value    | Final negotiated settlement.                                    |                                |
| continuous_property_value | Ongoing property valuation for surety.                          |                                |
| other_surety_type         | Other surety categories (gold/SIP/LIC).                         |                                |
| bank_guarantee_value      | Bank guarantee amount.                                          |                                |
| lic_policy_value          | LIC policy pledged amount.                                      |                                |
| own_signature_value       | Value attached to own-signature surety.                         |                                |
| sip_guarantee_value       | SIP guarantee value.                                            |                                |
| gold_guarantee_value      | Gold pledged value.                                             |                                |
| final_surety_status       | Final surety status (Pending/Approved).                         |                                |
| final_surety_approved     | Boolean surety approved.                                        |                                |
| document_upload           | File path(s) for supporting docs.                               | Request file locations.        |
| created_by                | Creator user.                                                   |                                |
| updated_by                | Updater user.                                                   |                                |
| payment_consent           | Applicant consent record.                                       |                                |
| md_consent_reply          | MD-level consent reply text/flag.                               |                                |
| payment_consent_status    | Consent workflow status.                                        |                                |
| is_consent_approved       | Boolean consent approved.                                       |                                |
| chit_id                   | Chit id.                                                        |                                |
| ticket_no                 | Ticket number.                                                  |                                |
| amount_type               | Charge category.                                                |                                |
| charge_type               | Specific charge name.                                           |                                |
| mode_of_payment           | Cash/Cheque/NEFT/UPI etc.                                       |                                |
| payment_type              | Full/Partial/Adjustment.                                        |                                |
| cashier_comment           | Cashier remarks.                                                |                                |
| cashier_executive         | Cashier id/name.                                                |                                |
| receipt_no                | Receipt number.                                                 |                                |
| charge_values             | JSON of GST/breakup.                                            | Request sample JSON keys.      |
| payment_charge_status     | Status (Collected/Approved/Pending).                            |                                |
| is_payment_charge_paid    | Boolean paid flag.                                              |                                |
| charge_paid_date          | Date payment realized.                                          |                                |
| payment_charge_approval   | Approval metadata/flag.                                         |                                |
| charge_amount             | Numeric amount charged.                                         |                                |
| full_name                 | Denormalized applicant name for quick lookup.                   |                                |
| createdAt                 | Created timestamp.                                              |                                |
| updatedAt                 | Updated timestamp.                                              |                                |
| trans_id                  | Bank/system transaction id.                                     |                                |
| payment_status            | Success/Failed/Bounced/Pending.                                 |                                |
| trans_date                | Transaction date/time.                                          |                                |
| mode_of_pay               | Instrument used.                                                |                                |
| cheque_no                 | Cheque number (if used).                                        |                                |
| cheque_bank_name          | Cheque issuing bank name.                                       |                                |
| cheque_date               | Cheque date.                                                    |                                |
| paying_amount             | Amount paid for the transaction.                                |                                |
| is_cheque_handed          | Boolean whether cheque physically collected.                    |                                |
| payment_first_approval    | First approval flag/id.                                         |                                |
| payment_final_approval    | Final approval flag/id.                                         |                                |
| withdrawan_date           | Date payment/entry withdrawn if applicable.                     |                                |

---

## Transferred

| Field                   | Description                           | Note                                            |
| ----------------------- | ------------------------------------- | ----------------------------------------------- |
| id                      | Transfer record id (system).          | Optional if vendor provides other mapping keys. |
| applicant_id            | Member id associated with transfer.   | Required.                                       |
| chit_id                 | Chit id.                              |                                                 |
| full_name               | Name of the transferred member.       |                                                 |
| ticket_no               | Ticket number transferred.            |                                                 |
| amount                  | Chit amount relevant to transfer.     |                                                 |
| received_amount         | Amount collected until transfer.      |                                                 |
| remaining_amount        | Outstanding amount after transfer.    |                                                 |
| duration                | Remaining duration or total duration. |                                                 |
| latest_paid_insNo       | Last paid installment number.         |                                                 |
| transfered_date         | Date of transfer.                     |                                                 |
| transfer_first_approval | First level approval.                 |                                                 |
| transfer_final_approval | Final approval.                       |                                                 |
| transfer_status         | Transfer workflow status.             |                                                 |
| createdAt               | Created timestamp.                    |                                                 |
| updatedAt               | Updated timestamp.                    |                                                 |
| transfer_reason         | Reason for transfer.                  |                                                 |
| created_by              | Creator user.                         |                                                 |
| updated_by              | Updater user.                         |                                                 |
| is_transfered_member    | Boolean marking transfer complete.    |                                                 |

---

### Final vendor instructions (copy into request)

1. **Provide CSV exports (UTF-8)** for each table above. One CSV per table, containing **all historical data from the beginning of the system until today**.
2. If the vendor cannot share PII columns as-is, they must provide **schema + sample anonymized values** for PII fields and confirm which columns are redacted.
3. For every JSON/complex column (e.g., `charge_values`, `property_security_value`) include **one sample row with the full JSON** and list the JSON keys.
4. For file/document columns (e.g., `personal_photo`, `aadhar_card`, `document_upload`) provide either the files zipped with matching filenames, or a table that maps filename → storage path → accessible method (SFTP/S3).
5. Provide **row counts** and **approximate date range** (earliest and latest timestamp) for each CSV.
6. If any column is encrypted/hashed, indicate encryption method and whether keys can be shared or redaction will remain.
7. Provide a **mapping file (CSV)** where vendor lists: original_table, original_column, example_value, notes — to speed mapping to our new schema.

