"""
Skrypt do optymalizacji obrazów WebP w różnych rozmiarach dla lepszego SEO.
Wymaga zainstalowania Pillow: pip install Pillow
"""

from PIL import Image
import os

def optimize_images():
    # Ścieżka do folderu z obrazami
    assets_dir = "assets"

    # Definicja rozmiarów dla różnych urządzeń
    sizes = {
        'small': 400,    # Mobile
        'medium': 800,   # Tablet
        'large': 1200,   # Desktop
    }

    # Lista plików do przetworzenia
    image_files = [
        'profilowe.webp',
        'ślubny1.webp',
        'ślubny2.webp',
        'ślubny3.webp',
        'kolorowy1.webp',
        'kolorowy2.webp',
        'kolorowy3.webp',
        'kolorowy4.webp',
        'kolorowy5.webp',
        'sylwestrowy1.webp'
    ]

    for image_file in image_files:
        image_path = os.path.join(assets_dir, image_file)

        if not os.path.exists(image_path):
            print(f"Plik nie istnieje: {image_path}")
            continue

        print(f"Przetwarzanie: {image_file}")

        # Otwórz obraz
        img = Image.open(image_path)

        # Nazwa pliku bez rozszerzenia
        file_name = os.path.splitext(image_file)[0]

        # Generuj różne rozmiary
        for size_name, width in sizes.items():
            # Oblicz nową wysokość zachowując proporcje
            ratio = width / img.width
            height = int(img.height * ratio)

            # Zmień rozmiar
            resized_img = img.resize((width, height), Image.Resampling.LANCZOS)

            # Zapisz z kompresją
            output_path = os.path.join(assets_dir, f"{file_name}-{size_name}.webp")
            resized_img.save(output_path, 'WEBP', quality=85, method=6)

            print(f"  ✓ Utworzono: {file_name}-{size_name}.webp ({width}x{height})")

    print("\n✅ Optymalizacja zakończona!")
    print("\nTeraz możesz użyć tych obrazów w HTML z atrybutem srcset:")
    print('<img src="assets/profilowe-medium.webp"')
    print('     srcset="assets/profilowe-small.webp 400w,')
    print('             assets/profilowe-medium.webp 800w,')
    print('             assets/profilowe-large.webp 1200w"')
    print('     sizes="(max-width: 640px) 400px, (max-width: 1024px) 800px, 1200px"')
    print('     alt="...">')

if __name__ == "__main__":
    try:
        optimize_images()
    except ImportError:
        print("❌ Błąd: Brakuje biblioteki Pillow")
        print("Zainstaluj ją komendą: pip install Pillow")
    except Exception as e:
        print(f"❌ Wystąpił błąd: {e}")

