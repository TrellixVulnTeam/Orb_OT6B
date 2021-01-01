/*
Orb Standard Library

Version Notes
    1.0
        First Commit
*/
#include <string>

#ifndef OPSLIB_HPP
#define OPSLIB_HPP


#define OPSLIB_VERSION "1.00.00"
#define OPSLIB_API_LEVEL "1.00.00"

namespace orb {
    /*初始化Orb
    bool orb::init_OPSLIB_API(string orb_path)
    
    :param orb_path(string) 指定Orb安装目录
    :return bool
    */
    bool init_OPSLIB(std::string orb_path);
} // namespace orb


#endif //OPSLIB_HPP
