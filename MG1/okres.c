#include <stdio.h>
#include <stdint.h>

struct RNG {
    uint32_t r;
    uint32_t a;
    uint32_t c;
    uint64_t m;
};

void init_rng(struct RNG rng, uint32_t seed) {
    rng->r = seed;
    rng->a = 1664525;
    rng->c = 1013904223;
    rng->m = 4294967296; // 2^32
}

double next(struct RNGrng) {
    rng->r = (rng->a * rng->r + rng->c) % rng->m;
    return ((double) rng->r) / rng->m;
}

int main() {
    struct RNG rng;
    uint32_t initial_seed = 4;
    init_rng(&rng, initial_seed);

    uint32_t first_value = rng.r;
    uint64_t count = 0;

    do {
        next(&rng);
        count++;
    } while(rng.r != first_value);

    printf("Okres generatora: %lu\n", count);

    return 0;
}