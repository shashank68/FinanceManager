BEGIN;
--
-- Create model Stocks
--
CREATE TABLE "FMapp_stocks" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Company_Name" text NOT NULL, "Company_Symbol" text NOT NULL, "Purchase_Date" date NOT NULL, "Purch
ase_Cost" decimal NOT NULL, "Quantity" integer NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Savings
--
CREATE TABLE "FMapp_savings" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Bank_Name" text NOT NULL, "Account_Number" text NOT NULL, "Balance" decimal NOT NULL, "Status" bo
ol NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Loans
--
CREATE TABLE "FMapp_loans" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Bank_Name" text NOT NULL, "Account_Number" text NOT NULL, "Balance" decimal NOT NULL, "Status" bool
 NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Expenditures
--
CREATE TABLE "FMapp_expenditures" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Amount" decimal NOT NULL, "Date" date NOT NULL, "Remarks" text NOT NULL, "user_id" integer N
OT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "FMapp_stocks_user_id_ae6f356a" ON "FMapp_stocks" ("user_id");
CREATE INDEX "FMapp_savings_user_id_80283ae1" ON "FMapp_savings" ("user_id");
CREATE INDEX "FMapp_loans_user_id_332a1534" ON "FMapp_loans" ("user_id");
CREATE INDEX "FMapp_expenditures_user_id_03a64eac" ON "FMapp_expenditures" ("user_id");
COMMIT;