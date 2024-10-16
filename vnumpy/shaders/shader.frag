#version 450

layout(binding = 1) uniform sampler2D texSampler;

layout(location = 0) in vec4 fragColor;
layout(location = 1) in vec2 fragTexCoord;

layout(location = 0) out vec4 outColor;

void main() {
    //outColor = fragColor;//texture(texSampler, fragTexCoord);
	// 硬编码的对比度调整
    float contrast = 1.3;  // 调整此值来设置对比度大小，1.0 表示没有调整
    vec4 color = fragColor;

    // 中心化颜色到 [0.5, 0.5, 0.5]，然后应用对比度
    color.rgb = (color.rgb - 0.5) * contrast + 0.5;

    // 限制颜色值在 [0.0, 1.0] 范围内，避免溢出
    color.rgb = clamp(color.rgb, 0.0, 1.0);

    outColor = color;  // 输出调整后的颜色
}