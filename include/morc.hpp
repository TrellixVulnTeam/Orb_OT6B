/*
Orb Core

Version Notes
    1.0
        First Commit
*/
#include <string>

#ifndef MORC_HPP
#define MORC_HPP


#define MORC_VERSION "1.00.00"
#define MORC_API_LEVEL "1.00.00"

// low char
#define port_request    33625
#define port_errorlog   33626
#define port_mcmd       33627
#define port_mpcore     33628
#define port_radio      33629
#define port_cservice   33630

namespace morc {
    typedef struct MORC_HANDLE {
        std::string sKEY;
    };
} // namespace morc


#endif //MORC_HPP
