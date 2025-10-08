import Image from 'next/image';

const Header = () => {
  return (
    <header className="bg-black/30 backdrop-blur-sm sticky top-0 z-50">
      <nav className="container mx-auto px-4 py-3">
        <Image 
          src="/GURE_ULTRA_RED_white.png" 
          alt="Gure Ultra Logo" 
          width={150} 
          height={40} 
          priority
        />
      </nav>
    </header>
  );
};

export default Header;