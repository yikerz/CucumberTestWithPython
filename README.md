# Generating and Viewing Allure Report for Behave Tests

## Generate Allure Report

To generate an Allure report for your Behave tests, use the following command:

```bash
behave -f allure_behave.formatter:AllureFormatter -o "reports" feature_file
```

## Open Report Using Browser

```powershell
allure serve reports
```