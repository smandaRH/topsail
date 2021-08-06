from toolbox._common import PlaybookRun


class Cluster:
    """
    Commands relating to cluster scaling, upgrading and environment capture
    """
    @staticmethod
    def set_scale(instance_type, scale, base_machineset="", force=False):
        """
        Ensures that the cluster has exactly `scale` nodes with instance_type `instance_type`

        If the machinesets of the given instance type already have the required total number of replicas,
        their replica parameters will not be modified.
        Otherwise,
        - If there's only one machineset with the given instance type, its replicas will be set to the value of this parameter.

        - If there are other machinesets with non-zero replicas, the playbook will fail, unless the 'force_scale' parameter is
        set to true. In that case, the number of replicas of the other machinesets will be zeroed before setting the replicas
        of the first machineset to the value of this parameter."

        Example: ./run_toolbox.py cluster set_scale g4dn.xlarge 1 # ensure that the cluster has 1 GPU node

        Args:
            instance_type: The instance type to use, for example, g4dn.xlarge
            scale: The number of required nodes with given instance type
            base_machineset: Name of a machineset to use to derive the new one. Defaults: pickup the first machineset found in `oc get machinesets -n openshift-machine-api`.
        """
        opts = {
                "machineset_instance_type": instance_type,
                "scale": scale,
                "base_machineset": base_machineset,
            }

        if force:
            opts["force_scale"] = "true"

        return PlaybookRun("cluster_set_scale", opts)

    @staticmethod
    def upgrade_to_image(image):
        """
        Upgrades the cluster to the given image

        Args:
            image: The image to upgrade the cluster to
        """
        return PlaybookRun("cluster_upgrade_to_image", {"cluster_upgrade_image": image})

    @staticmethod
    def capture_environment():
        """
        Captures the cluster environment

        Args:
            image: The image to upgrade the cluster to
        """
        return PlaybookRun("capture_environment")