cmake_minimum_required(VERSION 3.16)
project(RepackGuard VERSION 0.1.0 LANGUAGES C)

set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED ON)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Warnungen nicht als Fehler, aber sichtbar
add_compile_options(-Wall -Wextra)

# Kern-Bibliothek
add_library(rg_core STATIC src/rg_core.c)
target_include_directories(rg_core PUBLIC src)

# CLI
add_executable(rg_cli src/rg_cli.c)
target_link_libraries(rg_cli PRIVATE rg_core)

# Tests
enable_testing()
add_executable(test_core tests/test_core.c)
target_link_libraries(test_core PRIVATE rg_core)
add_test(NAME core COMMAND test_core)

# CLI-Tests: Exit-Codes und Ausgaben gegen die echten Testdaten
add_test(NAME cli_tests
         COMMAND bash ${CMAKE_SOURCE_DIR}/tests/run_cli_tests.sh
                 $<TARGET_FILE:rg_cli> ${CMAKE_SOURCE_DIR}/testdata)
