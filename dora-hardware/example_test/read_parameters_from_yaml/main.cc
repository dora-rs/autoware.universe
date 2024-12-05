// 文件路径: main.cpp
#include <iostream>
#include <yaml-cpp/yaml.h>

int main() {
    // YAML 文件路径
    std::string filePath = "config.yaml";

    try {
        // 加载 YAML 文件
        YAML::Node config = YAML::LoadFile(filePath);

        // 检查 lidar 键是否存在
        if (config["lidar"] && config["lidar"].IsSequence()) 
        {
            // 遍历 lidar 数组中的每个元素
            for (const auto& lidar_node : config["lidar"]) 
            {
                if (lidar_node["driver"]) 
                {
                    auto driver = lidar_node["driver"];
                    std::cout << "Lidar Type: " << driver["lidar_type"].as<std::string>() << std::endl;
                    std::cout << "Msop Port: " << driver["msop_port"].as<int>() << std::endl;
                    std::cout << "Difop Port: " << driver["difop_port"].as<int>() << std::endl;
                } 
                else 
                {
                    std::cout << "No 'driver' section found for lidar." << std::endl;
                }
            }
        } 
        else 
        {
            std::cout << "Lidar configuration not found or empty!" << std::endl;
        }
    } catch (const YAML::BadFile& e) {
        std::cerr << "无法打开 YAML 文件: " << filePath << std::endl;
        return 1;
    } catch (const YAML::Exception& e) {
        std::cerr << "解析 YAML 文件出错: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}

