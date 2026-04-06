using UnityEngine;
using Unity.XR.PXR;

public class VRHandController : MonoBehaviour
{
    [Header("控制器设置")]
    public DeviceType controllerType = DeviceType.RightController;
    
    [Header("射线设置")]
    public LineRenderer lineRenderer;
    public float rayLength = 10f;
    public LayerMask interactableLayer;
    
    [Header("抓取设置")]
    public Transform grabPoint;
    
    private VRInteractable currentInteractable;
    private VRInteractable grabbedObject;
    private bool isGrabbing = false;
    
    void Start()
    {
        // 初始化射线
        if (lineRenderer == null)
        {
            lineRenderer = gameObject.AddComponent<LineRenderer>();
            lineRenderer.startWidth = 0.01f;
            lineRenderer.endWidth = 0.01f;
            lineRenderer.positionCount = 2;
        }
        
        if (grabPoint == null)
        {
            grabPoint = transform;
        }
    }
    
    void Update()
    {
        UpdateRaycast();
        HandleInput();
    }
    
    void UpdateRaycast()
    {
        Ray ray = new Ray(transform.position, transform.forward);
        RaycastHit hit;
        
        // 更新射线可视化
        lineRenderer.SetPosition(0, transform.position);
        
        if (Physics.Raycast(ray, out hit, rayLength, interactableLayer))
        {
            lineRenderer.SetPosition(1, hit.point);
            
            // 检测到可交互物体
            VRInteractable interactable = hit.collider.GetComponent<VRInteractable>();
            if (interactable != null && interactable != currentInteractable)
            {
                // 离开上一个物体
                if (currentInteractable != null)
                {
                    currentInteractable.OnHoverExit();
                }
                
                // 进入新物体
                currentInteractable = interactable;
                currentInteractable.OnHoverEnter();
            }
        }
        else
        {
            lineRenderer.SetPosition(1, transform.position + transform.forward * rayLength);
            
            // 离开当前物体
            if (currentInteractable != null)
            {
                currentInteractable.OnHoverExit();
                currentInteractable = null;
            }
        }
    }
    
    void HandleInput()
    {
        // 抓取/释放 - 使用扳机键
        bool triggerDown = PXR_Input.GetControllerButtonDown(controllerType, PXR_Input.ControllerButton.RTrigger);
        bool triggerUp = PXR_Input.GetControllerButtonUp(controllerType, PXR_Input.ControllerButton.RTrigger);
        
        if (triggerDown)
        {
            if (grabbedObject == null && currentInteractable != null)
            {
                // 抓取物体
                grabbedObject = currentInteractable;
                grabbedObject.OnGrab(grabPoint);
                isGrabbing = true;
            }
        }
        else if (triggerUp)
        {
            if (grabbedObject != null)
            {
                // 释放物体
                grabbedObject.OnRelease();
                grabbedObject = null;
                isGrabbing = false;
            }
        }
        
        // A键 - 按钮交互
        if (PXR_Input.GetControllerButtonDown(controllerType, PXR_Input.ControllerButton.A))
        {
            OnButtonAPressed();
        }
        
        // B键 - 菜单/返回
        if (PXR_Input.GetControllerButtonDown(controllerType, PXR_Input.ControllerButton.B))
        {
            OnButtonBPressed();
        }
    }
    
    void OnButtonAPressed()
    {
        Debug.Log($"{controllerType} A键按下");
        
        // 可以在这里添加A键的特定功能
        // 例如：切换抓取模式、打开菜单等
    }
    
    void OnButtonBPressed()
    {
        Debug.Log($"{controllerType} B键按下");
        
        // 可以在这里添加B键的特定功能
        // 例如：打开系统菜单、返回等
    }
}
