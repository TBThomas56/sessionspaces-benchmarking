from kubernetes import client, config
import time

config.load_config()

start_time = time.time()
v1 = client.CoreV1Api()
v2 = client.RbacAuthorizationV1Api()
namespace = "workflows"
pods = v1.list_namespace()


pod_names = [pod.metadata.name for pod in pods.items]
print(f"Found {len(pod_names)} namespaces:")

# Get all configmaps
cm = 0
rbs_visit_member = 0
for namespace in pod_names:
    try:
        v1.read_namespaced_config_map("sessionspaces", namespace)
        cm += 1
        v2.read_namespaced_role_binding("visit-member", namespace)
        rbs_visit_member += 1
    except Exception:
        continue

print(f"Found Configmaps for {cm} namespaces")

end_time = time.time()
print(f"Time taken: {end_time - start_time:.2f} seconds")
print(f"Found {rbs_visit_member} visit-member rolebindings")

current_time = time.strftime("%Y-%m-%d %H:%M:%S")

with open("output.csv", "a") as file:
    file.write(f"{current_time},{len(pod_names)},{cm},{rbs_visit_member}\n")
