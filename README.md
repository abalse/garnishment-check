# Welcome, autobots-b, to the 2023 TDI Global Hackathon
## About your hackathon environment
Your hackathon environment consists of four components:
1. A GCP project (https://console.cloud.google.com/home/dashboard?project=hack-team-autobots-b)
2. This GitHub repository (https://github.com/db-hackathon/autobots-b)
3. A Terraform Cloud workspace (https://app.terraform.io/app/db-hackathon-2023/workspaces/hack-team-autobots-b)
4. A namespace in a shared RedHat Openshift 4.13 cluster (XXX)

You have considerable interactive access to your GCP project.
Using the GitHub repository and the Terraform Cloud workspace are entirely optional.

### [GCP](https://console.cloud.google.com/home/dashboard?project=hack-team-autobots-b)
#### First log-in
To log in to the GCP Cloud Console:
1. Navigate to https://console.cloud.google.com.
2. Sign out if you're already signed in.
3. On the first form (headed, "Sign in to continue to Google Cloud Platform") enter your hackathon user ID then click "Next".
   1. To derive your hackathon user ID, take the personal email address you signed up with, substitute the "@" with "." and append "@dbtechhackathon.com".
   2. For example, foo@bar.com becomes foo.bar.com@dbtechhackathon.com.
4. On the next form (headed, "Hi <name>"), click "Forgot password?".
5. Follow the password recovery process. It will send a link to your personal email address.
6. Follow that link and set a new password.
7. Set up 2FA immediately.
8. Navigate to https://console.cloud.google.com/home/dashboard?project=hack-team-autobots-b.

#### Access Rights & Actors
The below APIs have been activated on your project. You cannot activate APIs yourselves.
* aiplatform.googleapis.com
* artifactregistry.googleapis.com
* automl.googleapis.com
* bigquery.googleapis.com
* bigqueryconnection.googleapis.com
* cloudbuild.googleapis.com
* clouderrorreporting.googleapis.com
* cloudfunctions.googleapis.com
* cloudsupport.googleapis.com
* composer.googleapis.com
* contactcenteraiplatform.googleapis.com
* contactcenterinsights.googleapis.com
* dataflow.googleapis.com
* dataproc.googleapis.com
* dialogflow.googleapis.com
* documentai.googleapis.com
* language.googleapis.com
* logging.googleapis.com
* monitoring.googleapis.com
* notebooks.googleapis.com
* pubsub.googleapis.com
* run.googleapis.com
* servicemanagement.googleapis.com
* serviceusage.googleapis.com
* speech.googleapis.com
* sql-component.googleapis.com
* sqladmin.googleapis.com
* storage-api.googleapis.com
* storage-component.googleapis.com
* storagetransfer.googleapis.com
* texttospeech.googleapis.com
* translate.googleapis.com
* videointelligence.googleapis.com
* vision.googleapis.com
* workflowexecutions.googleapis.com
* workflows.googleapis.com
* workstations.googleapis.com

Every team member has the following roles granted at project level:
* roles/aiplatform.migrator
* roles/aiplatform.tensorboardWebAppUser
* roles/aiplatform.user
* roles/artifactregistry.admin
* roles/automl.editor
* roles/bigquery.connectionAdmin
* roles/bigquery.dataOwner
* roles/bigquery.resourceViewer
* roles/bigquery.user
* roles/bigquerydatapolicy.maskedReader
* roles/cloudbuild.builds.approver
* roles/cloudbuild.builds.editor
* roles/cloudbuild.connectionAdmin
* roles/cloudbuild.integrationsOwner
* roles/cloudbuild.integrationsViewer
* roles/cloudbuild.workerPoolOwner
* roles/cloudfunctions.developer
* roles/cloudsql.admin
* roles/cloudsupport.techSupportEditor
* roles/cloudtranslate.editor
* roles/composer.admin
* roles/contactcenteraiplatform.admin
* roles/contactcenterinsights.editor
* roles/dataflow.developer
* roles/dataproc.editor
* roles/dialogflow.admin
* roles/documentai.editor
* roles/errorreporting.admin
* roles/logging.admin
* roles/monitoring.editor
* roles/notebooks.admin
* roles/notebooks.legacyViewer
* roles/pubsub.editor
* roles/run.admin
* roles/servicemanagement.quotaViewer
* roles/serviceusage.serviceUsageConsumer
* roles/speech.editor
* roles/storage.admin
* roles/storagetransfer.admin
* roles/visionai.editor
* roles/workflows.editor
* roles/workstations.admin
* roles/workstations.networkAdmin

You have an "infrastructure SA" (infrastructure@hack-team-autobots-b.iam.gserviceaccount.com) with the same IAM permissions as team members.
You can authenticate as it from a GitHub Actions workflow anywhere in this repo using the Workload Identity Federation method of [Google's auth action](https://github.com/google-github-actions/auth)
and run gcloud commands using [Google's setup-gcloud Action](https://github.com/google-github-actions/setup-gcloud).
There's an example workflow in your repo to start you off.
This SA is also used when you provision infrastructure using your Terraform Cloud workspace.

You have a "workload SA" (workload@hack-team-autobots-b.iam.gserviceaccount.com) that you can use to attach to your workloads (e.g. Cloud Run revisions).
The default SAs have been de-privileged.
The workload SA has the following roles granted at project level:
* roles/aiplatform.user
* roles/artifactregistry.createOnPushWriter
* roles/automl.predictor
* roles/bigquery.connectionUser
* roles/bigquery.dataViewer
* roles/bigquery.filteredDataViewer
* roles/bigquery.jobUser
* roles/bigquery.readSessionUser
* roles/bigquerydatapolicy.maskedReader
* roles/cloudbuild.builds.builder
* roles/cloudbuild.tokenAccessor
* roles/cloudbuild.workerPoolUser
* roles/cloudfunctions.invoker
* roles/cloudsql.client
* roles/cloudsql.instanceUser
* roles/cloudtranslate.user
* roles/composer.worker
* roles/contactcenteraiplatform.viewer
* roles/contactcenterinsights.viewer
* roles/dataflow.worker
* roles/dataproc.hubAgent
* roles/dataproc.worker
* roles/dialogflow.client
* roles/dialogflow.reader
* roles/documentai.apiUser
* roles/errorreporting.writer
* roles/logging.logWriter
* roles/monitoring.metricWriter
* roles/notebooks.runner
* roles/pubsub.publisher
* roles/pubsub.subscriber
* roles/run.invoker
* roles/servicemanagement.quotaViewer
* roles/serviceusage.serviceUsageConsumer
* roles/speech.client
* roles/storage.objectViewer
* roles/storagetransfer.transferAgent
* roles/storagetransfer.user
* roles/visionai.admin
* roles/workflows.invoker

#### Limitations & Restrictions
* You have a budget of EUR ~700.
You will receive notifications when your actual or forecast spend passes 25%, 50%, 75%, 90% and 100%.
Your project will be torn down if you approach 100% or if you are spending rapidly. 
* Fairly severe quotas are in place to help manage the above.
Talk to the happy hackathon helpers if this is impeding your idea.
* The default compute SA in your project has been de-privileged.
Whenever you provision compute (e.g. a VMs powering a Jupyter notebook or dataflow pipeline, a Cloud Run service or a Cloud Function) 
you must attach the Workload SA, usually referred to in the GCP documentation as "attaching a custom SA".
* You cannot create services accounts.
  * Use your infrastructure SA to interact with GCP from GitHub.
  * Use your workload SA to power your workloads.
* You cannot create or upload service account keys.
  * Use your own interactive access or Workload Identity Federation from GitHub Actions workflows instead.

### [GitHub](https://github.com/db-hackathon/autobots-b)
This repository is at your disposal.
All team members have "maintainer" access.
No branch protection rules are enforced.

A set of useful [GitHub Actions variables](https://docs.github.com/en/actions/learn-github-actions/variables) have been populated for you:
* vars.INFRA_SA_EMAIL - The email address representation of the SA you can use to deploy infrastructure. It has the same access rights as human team members.: infrastructure@hack-team-autobots-b.iam.gserviceaccount.com
* vars.INFRA_SA_ID - The fully qualified ID representation of the SA you can use to deploy infrastructure.: projects/hack-team-autobots-b/serviceAccounts/infrastructure@hack-team-autobots-b.iam.gserviceaccount.com
* vars.PROJECT_ID - Your team's GCP Project ID.: hack-team-autobots-b
* vars.PROJECT_NUMBER - Your teams' GCP Project Number.: 183438095322
* vars.WORKLOAD_IDENTITY_PROVIDER - The ID of the Workload Identity provider you cah use to authenticate from GitHub Actions to your GCP project.: projects/785558430619/locations/global/workloadIdentityPools/github-2023/providers/github-2023
* vars.WORKLOAD_SA_EMAIL - The email address representation of the SA you can attach to your workloads (e.g. to a Cloud Run service). : workload@hack-team-autobots-b.iam.gserviceaccount.com
* vars.WORKLOAD_SA_ID - The fully qualified ID representation of the SA you can attach to your workloads (e.g. to a Cloud Run service). : projects/hack-team-autobots-b/serviceAccounts/workload@hack-team-autobots-b.iam.gserviceaccount.com

#### Limitations & Restrictions
* The hackathon platform owns the files that were seeded into this repo.
If you modify them, your changes may be overwritten.
* We have a hard limit of 50,000 GitHub Actions minutes for the whole hackathon.
We request heavy user consider offloading what they can to Cloud Build instead
* We have a hard limit of 50GB of GitHub Actions and Packages storage for the whole hackathon.
  * If you produce very large GitHub Actions logs, please clean them up in a timely manner.
  * If you want to publish container images, please use GCP Artifact Registry.
  * For other artefacts, consider using Cloud Storage.

### [Terraform Cloud](https://app.terraform.io/app/db-hackathon-2023/workspaces/hack-team-autobots-b)
Your Terraform Cloud workspace is VCS-backed by this GitHub repository.
Pushing files to the "terraform" directory of this repo will automatically trigger a plan/apply cycle in TFC 
using the contents of that directory as the root module.

The workspace has been pre-configured so that the google and google-beta providers will authenticate using your infrastructure SA 
and default to creating resources in your project.

A set of useful [Input variables](https://developer.hashicorp.com/terraform/language/values/variables) have been populated for you:
* infra_sa_email - The email address representation of the SA you can use to deploy infrastructure. It has the same access rights as human team members.: infrastructure@hack-team-autobots-b.iam.gserviceaccount.com
* infra_sa_id - The fully qualified ID representation of the SA you can use to deploy infrastructure.: projects/hack-team-autobots-b/serviceAccounts/infrastructure@hack-team-autobots-b.iam.gserviceaccount.com
* project_id - Your team's GCP Project ID.: hack-team-autobots-b
* project_number - Your teams' GCP Project Number.: 183438095322
* workload_identity_provider - The ID of the Workload Identity provider you cah use to authenticate from GitHub Actions to your GCP project.: projects/785558430619/locations/global/workloadIdentityPools/github-2023/providers/github-2023
* workload_sa_email - The email address representation of the SA you can attach to your workloads (e.g. to a Cloud Run service). : workload@hack-team-autobots-b.iam.gserviceaccount.com
* workload_sa_id - The fully qualified ID representation of the SA you can attach to your workloads (e.g. to a Cloud Run service). : projects/hack-team-autobots-b/serviceAccounts/workload@hack-team-autobots-b.iam.gserviceaccount.com

### OpenShift (XXX)
#### Interactive Access
Log in to OpenShift via https://console-openshift-console.apps.dbh.dbhackathon.org/.
No SSL cert has been provisioned, so you'll have to risk the warnings.
On that page, choose to "Log in with" the "githubidp" option and use the GitHub handle you signed up with to complete the authentication.
