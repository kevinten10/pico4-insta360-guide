using UnityEngine;
using Unity.XR.PXR;

public class HelloPICO : MonoBehaviour
{
    void Start()
    {
        Debug.Log("🎮 欢迎来到PICO 4 VR世界！");
        
        // 检查设备状态
        if (PXR_Plugin.System != null)
        {
            Debug.Log($"设备型号: {PXR_Plugin.System.pxrSystem}");
        }
    }

    void Update()
    {
        // 检测右手控制器A键按下
        if (PXR_Input.GetControllerButtonDown(DeviceType.RightController, PXR_Input.ControllerButton.A))
        {
            Debug.Log("👆 右手A键按下！");
            OnButtonPressed();
        }

        // 检测左手控制器X键按下
        if (PXR_Input.GetControllerButtonDown(DeviceType.LeftController, PXR_Input.ControllerButton.X))
        {
            Debug.Log("👈 左手X键按下！");
            OnButtonPressed();
        }

        // 检测头部晃动
        CheckHeadMovement();
    }

    void OnButtonPressed()
    {
        // 触发一个简单的视觉效果
        GetComponent<Renderer>()?.material.SetColor("_Color", Random.ColorHSV());
    }

    void CheckHeadMovement()
    {
        // 获取头部旋转
        Vector3 headRotation = Camera.main.transform.eulerAngles;
        
        // 可以在这里添加头部交互逻辑
    }
}
