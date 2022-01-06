from app import application
import config as cfg

def main():
    application.run(cfg.population_size, cfg.iterations, cfg.mutation_probability)

if __name__ == "__main__":
    main()
