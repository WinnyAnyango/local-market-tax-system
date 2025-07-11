import { Outlet } from 'react-router-dom';
import Header from './Header';
import Footer from './Footer';

const MainLayout = () => {
  return (
    <>
      <Header />
      <main>
        <Outlet /> {/* This renders the current page */}
      </main>
      <Footer />
    </>
  );
};

export default MainLayout;
