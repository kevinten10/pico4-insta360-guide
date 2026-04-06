using UnityEngine;
using Unity.XR.PXR;

public class VRPlayerController : MonoBehaviour
{
    [Header("移动设置")]
    public float moveSpeed = 2.0f;
    public float rotationSpeed = 90.0f;
    public bool useSnapTurn = true;
    public float snapTurnAngle = 45.0f;
    
    [Header("传送设置")]
    public LayerMask teleportLayer;
    public GameObject teleportMarkerPrefab;
    public float maxTeleportDistance = 10.0f;
    
    [Header("头部")]
    public Transform cameraTransform;
    
    private CharacterController characterController;
    private GameObject teleportMarker;
    private bool isTeleporting = false;
    private Vector3 moveDirection;
    
    void Start()
    {
        characterController = GetComponent<CharacterController>();
        if (characterController == null)
        {
            characterController = gameObject.AddComponent<CharacterController>();
            characterController.center = new Vector3(0, 1, 0);
            characterController.height = 2;
            characterController.radius = 0.3f;
        }
        
        // 创建传送标记
        if (teleportMarkerPrefab != null)
        {
            teleportMarker = Instantiate(teleportMarkerPrefab);
            teleportMarker.SetActive(false);
        }
        
        if (cameraTransform == null)
        {
            cameraTransform = Camera.main.transform;
        }
        
        Debug.Log("🎮 VR Player Controller 已启动");
    }
    
    void Update()
    {
        HandleMovement();
        HandleRotation();
        HandleTeleport();
        HandleHeadHeight();
    }
    
    void HandleMovement()
    {
        // 获取左手摇杆输入
        Vector2 primaryAxis = PXR_Input.GetControllerPrimary2DAxis(DeviceType.LeftController);
        
        if (primaryAxis.magnitude > 0.1f)
        {
            // 获取头部方向（忽略Y轴）
            Vector3 forward = cameraTransform.forward;
            Vector3 right = cameraTransform.right;
            
            forward.y = 0;
            right.y = 0;
            forward.Normalize();
            right.Normalize();
            
            // 计算移动方向
            moveDirection = (forward * primaryAxis.y + right * primaryAxis.x) * moveSpeed;
            moveDirection.y = -9.8f * Time.deltaTime; // 重力
            
            characterController.Move(moveDirection * Time.deltaTime);
        }
    }
    
    void HandleRotation()
    {
        // 获取右手摇杆输入
        Vector2 secondaryAxis = PXR_Input.GetControllerPrimary2DAxis(DeviceType.RightController);
        
        if (useSnapTurn)
        {
            // 快速转向
            if (secondaryAxis.x > 0.8f)
            {
                transform.Rotate(Vector3.up, snapTurnAngle);
            }
            else if (secondaryAxis.x < -0.8f)
            {
                transform.Rotate(Vector3.up, -snapTurnAngle);
            }
        }
        else
        {
            // 平滑旋转
            transform.Rotate(Vector3.up, secondaryAxis.x * rotationSpeed * Time.deltaTime);
        }
    }
    
    void HandleTeleport()
    {
        // 右手扳机键控制传送
        bool triggerPressed = PXR_Input.GetControllerButton(DeviceType.RightController, PXR_Input.ControllerButton.RTrigger);
        bool triggerDown = PXR_Input.GetControllerButtonDown(DeviceType.RightController, PXR_Input.ControllerButton.RTrigger);
        
        if (triggerPressed)
        {
            ShowTeleportMarker();
        }
        else if (isTeleporting && !triggerPressed)
        {
            DoTeleport();
        }
    }
    
    void ShowTeleportMarker()
    {
        Ray ray = new Ray(cameraTransform.position, cameraTransform.forward);
        RaycastHit hit;
        
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
            Vector3 teleportPos = teleportMarker.transform.position;
            teleportPos.y = transform.position.y; // 保持当前高度
            transform.position = teleportPos;
            teleportMarker.SetActive(false);
            
            Debug.Log("✨ 传送完成!");
        }
        isTeleporting = false;
    }
    
    void HandleHeadHeight()
    {
        // 根据头部位置调整角色控制器高度
        if (cameraTransform != null)
        {
            float headHeight = cameraTransform.localPosition.y;
            if (headHeight > 0.5f && headHeight < 2.5f)
            {
                characterController.height = headHeight;
                characterController.center = new Vector3(0, headHeight / 2, 0);
            }
        }
    }
}
