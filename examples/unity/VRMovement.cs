using UnityEngine;
using Unity.XR.PXR;

public class VRMovement : MonoBehaviour
{
    [Header("移动设置")]
    public float moveSpeed = 2.0f;
    public float rotationSpeed = 90.0f;
    public bool useSnapTurn = true;
    public float snapTurnAngle = 45.0f;

    [Header("传送设置")]
    public LayerMask teleportLayer;
    public GameObject teleportMarker;
    public float maxTeleportDistance = 10.0f;

    private CharacterController characterController;
    private Vector3 moveDirection;
    private bool isTeleporting = false;

    void Start()
    {
        characterController = GetComponent<CharacterController>();
        if (teleportMarker != null)
        {
            teleportMarker.SetActive(false);
        }
    }

    void Update()
    {
        HandleMovement();
        HandleRotation();
        HandleTeleport();
    }

    void HandleMovement()
    {
        Vector2 primaryAxis = PXR_Input.GetControllerPrimary2DAxis(DeviceType.LeftController);
        
        Camera vrCamera = Camera.main;
        Vector3 forward = vrCamera.transform.forward;
        Vector3 right = vrCamera.transform.right;
        
        forward.y = 0;
        right.y = 0;
        forward.Normalize();
        right.Normalize();

        moveDirection = (forward * primaryAxis.y + right * primaryAxis.x) * moveSpeed;
        moveDirection.y = -9.8f; // 重力

        characterController.Move(moveDirection * Time.deltaTime);
    }

    void HandleRotation()
    {
        Vector2 secondaryAxis = PXR_Input.GetControllerPrimary2DAxis(DeviceType.RightController);

        if (useSnapTurn)
        {
            if (secondaryAxis.x > 0.8f)
            {
                SnapRotate(snapTurnAngle);
            }
            else if (secondaryAxis.x < -0.8f)
            {
                SnapRotate(-snapTurnAngle);
            }
        }
        else
        {
            transform.Rotate(Vector3.up, secondaryAxis.x * rotationSpeed * Time.deltaTime);
        }
    }

    void SnapRotate(float angle)
    {
        transform.Rotate(Vector3.up, angle);
    }

    void HandleTeleport()
    {
        bool triggerPressed = PXR_Input.GetControllerButton(DeviceType.RightController, PXR_Input.ControllerButton.RTrigger);

        if (triggerPressed)
        {
            ShowTeleportMarker();
        }
        else if (isTeleporting)
        {
            DoTeleport();
        }
    }

    void ShowTeleportMarker()
    {
        RaycastHit hit;
        Ray ray = new Ray(Camera.main.transform.position, Camera.main.transform.forward);

        if (Physics.Raycast(ray, out hit, maxTeleportDistance, teleportLayer))
        {
            if (teleportMarker != null)
            {
                teleportMarker.SetActive(true);
                teleportMarker.transform.position = hit.point;
            }
            isTeleporting = true;
        }
        else
        {
            if (teleportMarker != null)
            {
                teleportMarker.SetActive(false);
            }
            isTeleporting = false;
        }
    }

    void DoTeleport()
    {
        if (teleportMarker != null && teleportMarker.activeSelf)
        {
            transform.position = teleportMarker.transform.position;
            teleportMarker.SetActive(false);
        }
        isTeleporting = false;
    }
}
