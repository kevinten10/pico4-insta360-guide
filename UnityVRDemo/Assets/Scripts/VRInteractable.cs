using UnityEngine;
using Unity.XR.PXR;

public class VRInteractable : MonoBehaviour
{
    [Header("交互设置")]
    public bool isGrabbable = true;
    public bool isTouchable = true;
    public bool usePhysics = true;
    
    [Header("视觉效果")]
    public Material highlightMaterial;
    public Material originalMaterial;
    
    [Header("音效")]
    public AudioClip grabSound;
    public AudioClip releaseSound;
    
    private bool isGrabbed = false;
    private Transform grabPoint;
    private Rigidbody rb;
    private Renderer rend;
    private AudioSource audioSource;
    
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        rend = GetComponent<Renderer>();
        audioSource = GetComponent<AudioSource>();
        
        if (audioSource == null && (grabSound != null || releaseSound != null))
        {
            audioSource = gameObject.AddComponent<AudioSource>();
        }
        
        if (originalMaterial == null && rend != null)
        {
            originalMaterial = rend.material;
        }
        
        // 确保有碰撞体
        if (GetComponent<Collider>() == null)
        {
            gameObject.AddComponent<BoxCollider>();
        }
    }
    
    public void OnHoverEnter()
    {
        if (highlightMaterial != null && rend != null)
        {
            rend.material = highlightMaterial;
        }
        
        // 放大效果
        transform.localScale *= 1.05f;
    }
    
    public void OnHoverExit()
    {
        if (originalMaterial != null && rend != null)
        {
            rend.material = originalMaterial;
        }
        
        // 恢复大小
        transform.localScale /= 1.05f;
    }
    
    public void OnGrab(Transform controllerTransform)
    {
        if (!isGrabbable) return;
        
        isGrabbed = true;
        grabPoint = controllerTransform;
        
        if (rb != null)
        {
            rb.useGravity = false;
            rb.isKinematic = true;
        }
        
        // 播放音效
        if (grabSound != null && audioSource != null)
        {
            audioSource.PlayOneShot(grabSound);
        }
        
        Debug.Log($"🤏  grabbed: {gameObject.name}");
    }
    
    public void OnRelease()
    {
        if (!isGrabbed) return;
        
        isGrabbed = false;
        grabPoint = null;
        
        if (rb != null)
        {
            rb.useGravity = true;
            rb.isKinematic = false;
        }
        
        // 播放音效
        if (releaseSound != null && audioSource != null)
        {
            audioSource.PlayOneShot(releaseSound);
        }
        
        Debug.Log($"👋 Released: {gameObject.name}");
    }
    
    void Update()
    {
        if (isGrabbed && grabPoint != null)
        {
            // 跟随控制器
            transform.position = grabPoint.position;
            transform.rotation = grabPoint.rotation;
        }
    }
    
    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("VRController"))
        {
            OnHoverEnter();
        }
    }
    
    void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("VRController"))
        {
            OnHoverExit();
        }
    }
}
