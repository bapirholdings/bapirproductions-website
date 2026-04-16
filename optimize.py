import os
import re

def minify_css(css):
    # Remove comments and whitespace
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    css = re.sub(r'\s+', ' ', css)
    return css.strip()

def minify_html(html):
    # Basic HTML minification (removes newlines and extra spaces)
    html = re.sub(r'>\s+<', '><', html)
    return html.strip()

def optimize_for_mobile():
    print("🚀 Starting Mobile Site Optimization...")
    
    # Create a 'dist' folder for the optimized files
    if not os.path.exists('dist'):
        os.makedirs('dist')

    files_to_process = {
        'html': ['index.html', 'about.html', 'portfolio.html', 'contact.html'],
        'css': ['style.css'],
        'js': ['script.js']
    }

    for ext, files in files_to_process.items():
        for file in files:
            if os.path.exists(file):
                with open(file, 'r') as f:
                    content = f.read()
                
                # Apply minification logic
                if ext == 'css':
                    optimized = minify_css(content)
                elif ext == 'html':
                    optimized = minify_html(content)
                else:
                    optimized = content # JS usually requires a specialized library like terser

                with open(f'dist/{file}', 'w') as f:
                    f.write(optimized)
                print(f"✅ Optimized {file} -> dist/{file}")

    print("\nOptimization complete! Use the files in the 'dist' folder for your live website.")

if __name__ == "__main__":
    optimize_for_mobile()
    
import os
try:
    from PIL import Image  # type: ignore[import]  # Ensure you run 'pip install Pillow'
    _HAS_PIL = True
except ModuleNotFoundError:
    Image = None
    _HAS_PIL = False
    print("⚠️ Pillow (PIL) is not installed; image optimization will be skipped. Run: pip install Pillow")

def optimize_asset_folders():
    # The specific folders you mentioned
    if not _HAS_PIL:
        print("⚠️ Pillow not available; skipping asset optimization.")
        return

    folders = ['visuals', 'logos']
    quality = 75 # Balance between quality and file size
    
    print("🎬 Starting Bapir Productions Asset Optimization...")

    for folder in folders:
        if not os.path.exists(folder):
            print(f"⚠️ Folder '{folder}' not found. Skipping...")
            continue
            
        print(f"--- Optimizing images in: {folder} ---")
        for filename in os.listdir(folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                filepath = os.path.join(folder, filename)
                try:
                    with Image.open(filepath) as img:
                        # Convert to RGB if needed (for PNG to JPEG conversion)
                        if img.mode in ("RGBA", "P"):
                            img = img.convert("RGB")
                        
                        # Save the optimized version, overwriting the original
                        img.save(filepath, optimize=True, quality=quality)
                        print(f"✅ Optimized: {filename}")
                except Exception as e:
                    print(f"❌ Could not optimize {filename}: {e}")

if __name__ == "__main__":
    optimize_asset_folders()