set(SRC_FILES
        GraphicUtilities.cpp)

set(HDR_FILES
        GraphicUtilities.h)

add_library(utilities
    ${SRC_FILES}
    ${HDR_FILES})

target_include_directories(utilities
    PUBLIC
            ${CMAKE_CURRENT_SOURCE_DIR})