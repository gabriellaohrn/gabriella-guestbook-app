Guestbook - Gabriella (Grupp 5)
Detta projekt innehåller en gästbok med frontend, backend och databas som hanteras via ArgoCD i OpenShift.

URL till applikationen
http://gabriella-python-route-grupp5.apps.devops24.cloud2.se/

Om projektet
Applikationen uppfyller krav för persistens och skalbarhet.

Inlägg sparas i en PostgreSQL-databas och är tillgängliga även i inkognitoläge eller vid omstart av poddar.

Skalning testas genom att ändra värdet för replicas i filerna backend/deployment.yaml eller frontend/deployment.yaml.

Resurshantering och namngivning
Alla resurser i detta projekt (Secrets, PVC, Services m.m.) är namngivna med prefixet Gabriella för att undvika krockar med andra klasskompisars resurser i samma namespace.

I händelse av underhåll eller felsökning kan existerande resurser raderas för att tvinga fram en nystart via ArgoCD. Vid radering av gabriella-db-pvc försvinner sparad data i gästboken.

Teknisk stack
Backend: Go

Frontend: Nginx

Databas: PostgreSQL

Verktyg: ArgoCD, OpenShift, GitHub Actions

Instruktioner för nystart
Om miljön behöver nollställas, utför följande steg i terminalen:

oc delete pvc gabriella-db-pvc -n grupp5

oc delete pod -l app=gabriella-db -n grupp5

Synka i ArgoCD.

Hur du hittar URL
Du hittar URL i OpenShift-konsolen:

Gå till Networking -> Routes.

Leta efter gabriella-frontend.

Kopiera adressen som står under Location.
