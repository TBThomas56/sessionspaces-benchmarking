import matplotlib.pyplot as plt
import csv
from datetime import datetime

# File Order
# f"{current_time},{len(pod_names)},{cm},{rbs_visit_member}\n"

time = []
namespaces_created = []
cm = []
visit_members = []

with open("output.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # row: [current_time, len(pod_names), rbs_visit_member, rbs_argo_workflow]
        time.append(datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S").strftime("%H:%M:%S"))
        namespaces_created.append(int(row[1]))
        cm.append(int(row[2]))
        visit_members.append(int(row[3]))

plt.plot(time, namespaces_created, label="Namespaces Created")
plt.plot(time, cm, label="Config Maps Created")
plt.plot(time, visit_members, label="Visit Member Role Binding")
plt.xlabel("Time")
plt.ylabel("Found Resources")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
